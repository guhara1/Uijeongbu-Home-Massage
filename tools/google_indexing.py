#!/usr/bin/env python3
"""구글 Indexing API 일괄 색인 통보 (선택).

구글은 IndexNow에 참여하지 않으므로, 구글에 즉시 색인을 알리려면
Indexing API(또는 Search Console URL 검사)를 사용한다.

사전 준비:
    1) Google Cloud Console에서 프로젝트 생성 → "Indexing API" 사용 설정
    2) 서비스 계정 생성 → JSON 키 발급 → tools/google-sa.json 으로 저장
       (google-sa.json 은 .gitignore 에 포함되어 커밋되지 않음)
    3) Search Console 속성(https://uijeongbu-home-massage.pages.dev/)에
       서비스 계정 이메일을 "소유자"로 추가
    4) pip install google-auth requests

사용법:
    python tools/google_indexing.py            # sitemap.xml의 모든 URL 통보
    python tools/google_indexing.py https://.../a/   # 특정 URL만

참고: Indexing API는 공식적으로 JobPosting/BroadcastEvent 구조화 데이터 페이지를
대상으로 안내되지만, 일반 URL의 색인 갱신 통보에도 널리 사용된다. 대량/반복 남용은
피하고, 새 글·중요 변경 시에만 호출하는 것을 권장한다.
"""
import os
import sys
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SA_PATH = os.path.join(ROOT, "tools", "google-sa.json")
SCOPES = ["https://www.googleapis.com/auth/indexing"]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"


def urls_from_sitemap(path):
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    root = ET.parse(path).getroot()
    return [loc.text for loc in root.findall(".//s:loc", ns)]


def main():
    if not os.path.exists(SA_PATH):
        print(f"서비스 계정 키가 없습니다: {SA_PATH}")
        print("README의 '구글 Indexing API' 안내를 참고해 설정하세요.")
        sys.exit(1)
    try:
        import requests
        from google.oauth2 import service_account
        from google.auth.transport.requests import AuthorizedSession
    except ImportError:
        print("필요 패키지가 없습니다. 먼저: pip install google-auth requests")
        sys.exit(1)

    if len(sys.argv) > 1:
        urls = sys.argv[1:]
    else:
        urls = urls_from_sitemap(os.path.join(ROOT, "sitemap.xml"))

    creds = service_account.Credentials.from_service_account_file(
        SA_PATH, scopes=SCOPES)
    session = AuthorizedSession(creds)

    ok = 0
    for u in urls:
        resp = session.post(ENDPOINT, json={"url": u, "type": "URL_UPDATED"})
        if resp.status_code == 200:
            ok += 1
            print(f"OK  {u}")
        else:
            print(f"ERR {resp.status_code}  {u}  {resp.text[:160]}")
    print(f"\n구글 Indexing API: {ok}/{len(urls)}건 통보 완료")


if __name__ == "__main__":
    main()
