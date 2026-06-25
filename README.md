# 의정부 출장마사지 사이트

경기도 의정부시 전지역 방문 관리 서비스(출장마사지·홈타이) 안내 정적 사이트입니다.

**상호**: 88마사지  
**전화예약**: 0508-202-4719

## 구조

- **정적 HTML 사이트** — 어느 호스팅(GitHub Pages, Cloudflare Pages, 웹서버)에서든 그대로 서빙 가능
- **build.py** + **content/** — 페이지를 Python으로 정의하고 정적 HTML 생성
- **생성물** — 각 디렉터리의 `index.html`, `sitemap.xml`, `robots.txt`

```
build.py                    # 빌드 스크립트
content/
  site.py                  # 상호·전화·도메인·메뉴
  main.py                  # 의정부 홈 (사이트 루트 / 메인 페이지)
  areas.py                 # 지역별 페이지 (16개)
  stations.py              # 역세권 페이지 (20개)
  areas_and_stations.py    # 생활권 페이지 (13개)
  info.py                  # 정보 페이지 (예약·확인사항·가이드·개인정보·고객센터)
assets/
  style.css                # 프리미엄 다크 + 오렌지 + 샴페인 골드 + Pretendard
  nav.js                   # 모바일 네비게이션
index.html                  # 생성된 의정부 홈 (사이트 루트)
gyeonggi/uijeongbu/<슬러그>/  # 지역·역세권·생활권 페이지
```

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수 리포트가 출력됩니다.

## URL 구조

- 의정부 홈: `/` (사이트 루트)
- 지역: `/gyeonggi/uijeongbu/<동슬러그>/` (예: `/gyeonggi/uijeongbu/minrak-dong/`)
- 역세권: `/gyeonggi/uijeongbu/station/<역슬러그>/`
- 생활권: `/gyeonggi/uijeongbu/area/<생활권슬러그>/`
- 정보: `/reservation/`, `/check/`, `/guide/`, `/support/`, `/support/privacy/`

## SEO 운영 원칙

- 본문 **2,000자 미만 페이지는 자동 `noindex`** 처리
- 의정부는 행정구가 없으므로 **구별 페이지 없음**
- 의정부1·2동, 호원1·2동, 신곡1·2동, 송산1·2·3동은 대표 동/생활권으로 통합
- 역명 기준 1개 URL (회룡역 등 환승역도 노선별로 쪼개지 않음, 출구별 페이지 없음)
- 상단·하단 메뉴에 키워드("출장마사지") 반복 없음, URL에 `-chuljangmassage`·`-hometai`·`-massage` 없음
- 모든 페이지 본문은 고유 작성 (지역명만 바꾼 복붙 없음)
- 메인페이지부터 모든 지역 페이지까지 내부링크 롱테일 키워드 강화 + 권위 있는 외부 링크(의정부시청·위키백과) 연결
- 예약 전 확인사항·개인정보 처리 기준·불법/선정적 서비스 불가 안내 필수 포함

## 스키마(JSON-LD)

모든 페이지에 자동 주입:
- `Organization` (전 페이지 공통)
- `WebPage` + `BreadcrumbList` (서브 페이지)
- 메인: `HealthAndBeautyBusiness`, `FAQPage`, `BreadcrumbList`, `ImageObject`(선호 썸네일)

> 실제 오프라인 사업장 주소가 없는 방문형 서비스이므로 `LocalBusiness` 스키마는 사용하지 않습니다.

## 페이지 구성

- 메인 1 + 지역 16 + 역세권 20 + 생활권 13 + 정보 5 = **55개**

## 빠른 색인(인덱싱) 설정

빌드 시 다음이 자동 생성된다:
- `sitemap.xml` — `<lastmod>` 포함, 색인 허용 페이지 전체
- `rss.xml` — RSS 2.0 피드(모든 페이지에 autodiscovery `<link rel="alternate">` 삽입)
- `robots.txt` — 전체 크롤 허용 + 네이버(Yeti) 명시 + `sitemap.xml`·`rss.xml` 안내
- `<INDEXNOW_KEY>.txt` — IndexNow 소유권 확인용 키 파일(루트 노출)
- 모든 페이지 `<head>`에 `naver-site-verification` 메타(구글은 `GOOGLE_VERIFICATION` 입력 시 함께 출력)

### 소유확인 / 사이트맵 제출
1. **네이버 서치어드바이저** — 사이트 등록 후 소유확인(메타 태그 이미 삽입됨) → `sitemap.xml`, `rss.xml` 제출
2. **구글 서치콘솔** — 속성 등록(필요 시 `content/site.py`의 `GOOGLE_VERIFICATION`에 메타 키 입력 후 재빌드) → `sitemap.xml` 제출
3. **빙 웹마스터** — 사이트 등록 → 사이트맵 제출(IndexNow와 연동)

### IndexNow (빙·네이버·얀덱스 즉시 통보)
글을 올리거나 수정할 때마다 즉시 색인을 통보한다.

```bash
python build.py            # 사이트 재생성 (sitemap·rss·키파일 갱신)
python tools/indexnow.py   # sitemap.xml의 모든 URL을 IndexNow로 일괄 통보
# 특정 URL만:
python tools/indexnow.py https://uijeongbu-home-massage.pages.dev/gyeonggi/uijeongbu/minrak-dong/
```
> 키 파일(`/<INDEXNOW_KEY>.txt`)이 실제 배포되어 열려야 통보가 수락된다. 첫 배포 후 한 번 `python tools/indexnow.py`를 실행하면 전체 URL이 빙·네이버에 즉시 전달된다.

### 구글 Indexing API (선택, 구글은 IndexNow 미참여)
`tools/google_indexing.py` — 서비스 계정으로 구글에 즉시 색인 통보.
설정: Google Cloud에서 Indexing API 사용 설정 → 서비스 계정 JSON을 `tools/google-sa.json`(커밋 제외)으로 저장 → Search Console 속성에 서비스 계정을 소유자로 추가 → `pip install google-auth requests` → `python tools/google_indexing.py`.

> 구글·빙의 익명 **sitemap ping** 엔드포인트는 2023년 폐지되었으므로, 구글은 서치콘솔/ Indexing API, 빙·네이버는 IndexNow를 사용한다.

## 배포 전 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경 후 `python3 build.py` 재실행
2. 네이버 서치어드바이저·구글 서치콘솔·빙 웹마스터에 사이트 등록 및 `sitemap.xml`/`rss.xml` 제출
3. 첫 배포 후 `python tools/indexnow.py` 1회 실행(전체 URL 즉시 통보)
4. 텔레그램 문의 링크(`TELEGRAM_BUILD`, `TELEGRAM_PARTNER`)를 실제 계정으로 확인

## 특징

- **프리미엄 다크 팔레트**: 딥 옵시디언 네이비 + 오렌지 #FF6B35 + 샴페인 골드 액센트
- **컴포넌트 오버레이**: 카드 샤인, 섹션 워밍 글로우, 글래스 요금 블록, 오렌지 그라데이션 버튼
- **Pretendard 폰트**: 한국식 산세리프 (최상의 가독성)
- **반응형 디자인** · **접근성(WAI-ARIA)** · **정적 HTML(빠른 로딩)**

## 컨텍스트

의정부시는 행정구가 없는 도시로, 1호선·7호선·의정부경전철을 따라 원도심 상권, 환승 생활권, 시청·행정 생활권, 동부 신도시(민락·고산) 주거 생활권, 외곽 차량 이동권으로 생활권이 뚜렷이 나뉩니다. 사용자가 예약 전 정확한 방문 가능 지역과 확인사항을 파악할 수 있도록 설계했으며, 구글 상위노출 정책(E-E-A-T, 도움되는 콘텐츠, Who/How/Why)을 반영했습니다.
