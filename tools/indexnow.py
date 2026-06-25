#!/usr/bin/env python3
"""IndexNow 일괄 색인 통보.

빙(Bing)·네이버·얀덱스 등 IndexNow 참여 검색엔진에 URL 변경을 즉시 알린다.
하나의 엔드포인트(api.indexnow.org)로 제출하면 참여 엔진 전체에 공유된다.

사용법:
    python tools/indexnow.py                # sitemap.xml의 모든 URL 통보
    python tools/indexnow.py https://.../a/ https://.../b/   # 특정 URL만 통보

사전 준비:
    1) python build.py 를 먼저 실행해 sitemap.xml 과 <KEY>.txt 를 생성/배포한다.
    2) 사이트가 실제로 배포되어 https://<도메인>/<KEY>.txt 가 열려야 한다.
       (검색엔진이 키 파일로 소유권을 확인한다)
"""
import json
import os
import sys
import urllib.request
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOST = BASE_URL.split("://", 1)[1].strip("/")
KEY_LOCATION = f"{BASE_URL.rstrip('/')}/{INDEXNOW_KEY}.txt"
ENDPOINT = "https://api.indexnow.org/indexnow"


def urls_from_sitemap(path: str):
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    root = ET.parse(path).getroot()
    return [loc.text for loc in root.findall(".//s:loc", ns)]


def submit(urls):
    if not urls:
        print("통보할 URL이 없습니다.")
        return
    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print(f"IndexNow 응답: {r.status} {r.reason}  ({len(urls)}건 통보)")
            print("→ 빙·네이버·얀덱스 등 IndexNow 참여 엔진에 전달됩니다.")
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code}: {e.reason}")
        print(e.read().decode("utf-8", "ignore")[:500])


def main():
    if not INDEXNOW_KEY:
        print("content/site.py 의 INDEXNOW_KEY 가 비어 있습니다.")
        sys.exit(1)
    if len(sys.argv) > 1:
        urls = sys.argv[1:]
    else:
        sm = os.path.join(ROOT, "sitemap.xml")
        if not os.path.exists(sm):
            print("sitemap.xml 이 없습니다. 먼저 python build.py 를 실행하세요.")
            sys.exit(1)
        urls = urls_from_sitemap(sm)
    print(f"{len(urls)}개 URL → IndexNow ({HOST})")
    submit(urls)


if __name__ == "__main__":
    main()
