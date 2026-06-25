# 의정부시 출장마사지 사이트 공통 설정

BASE_URL = "https://uijeongbu-home-massage.pages.dev"

BRAND = "88마사지"
BRAND_MARK = "88"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 메인 진입 경로 (의정부 홈 = 사이트 루트)
HOME = "/"

# 검색엔진 사이트 소유확인
NAVER_VERIFICATION = "fe84041b6962ae75f891ac0df183c7854db3377b"
GOOGLE_VERIFICATION = ""  # 구글 서치콘솔 메타 발급 시 입력

# IndexNow 키 (빙·네이버·얀덱스 등 즉시 색인 통보). 루트에 <KEY>.txt 로도 노출된다.
INDEXNOW_KEY = "6b1bf68219744b03965fe2ec423badb037c793c11e1649f7ba6f1ecc29f9e207"

# 외부 문의 링크 (텔레그램)
TELEGRAM_BUILD = "https://t.me/googleseolab"     # 웹사이트 제작문의
TELEGRAM_PARTNER = "https://t.me/googleseolab"   # 제휴문의

# 상단 메뉴 — 키워드 반복 없음, 지역명·역명만 표시 (지시서 §4)
NAV = [
    ("의정부 홈", HOME, []),
    ("지역별 안내", HOME, [
        ("의정부동", "/gyeonggi/uijeongbu/uijeongbu-dong/"),
        ("호원동", "/gyeonggi/uijeongbu/howon-dong/"),
        ("장암동", "/gyeonggi/uijeongbu/jangam-dong/"),
        ("신곡동", "/gyeonggi/uijeongbu/singok-dong/"),
        ("민락동", "/gyeonggi/uijeongbu/minrak-dong/"),
        ("낙양동", "/gyeonggi/uijeongbu/nagyang-dong/"),
        ("용현동", "/gyeonggi/uijeongbu/yonghyeon-dong/"),
        ("금오동", "/gyeonggi/uijeongbu/geumo-dong/"),
        ("가능동", "/gyeonggi/uijeongbu/ganeung-dong/"),
        ("흥선동", "/gyeonggi/uijeongbu/heungseon-dong/"),
        ("녹양동", "/gyeonggi/uijeongbu/nogyang-dong/"),
        ("고산동", "/gyeonggi/uijeongbu/gosan-dong/"),
        ("산곡동", "/gyeonggi/uijeongbu/sangok-dong/"),
        ("자일동", "/gyeonggi/uijeongbu/jail-dong/"),
        ("송산 생활권", "/gyeonggi/uijeongbu/songsan-area/"),
        ("자금 생활권", "/gyeonggi/uijeongbu/jageum-area/"),
    ]),
    ("역세권 안내", HOME, [
        ("의정부역", "/gyeonggi/uijeongbu/station/uijeongbu-station/"),
        ("회룡역", "/gyeonggi/uijeongbu/station/hoeryong-station/"),
        ("망월사역", "/gyeonggi/uijeongbu/station/mangwolsa-station/"),
        ("가능역", "/gyeonggi/uijeongbu/station/ganeung-station/"),
        ("녹양역", "/gyeonggi/uijeongbu/station/nogyang-station/"),
        ("장암역", "/gyeonggi/uijeongbu/station/jangam-station/"),
        ("경전철의정부역", "/gyeonggi/uijeongbu/station/light-rail-uijeongbu-station/"),
        ("의정부시청역", "/gyeonggi/uijeongbu/station/uijeongbu-cityhall-station/"),
        ("의정부중앙역", "/gyeonggi/uijeongbu/station/uijeongbu-jungang-station/"),
        ("동오역", "/gyeonggi/uijeongbu/station/dongo-station/"),
        ("경기도청북부청사역", "/gyeonggi/uijeongbu/station/gyeonggi-provincial-government-northern-office-station/"),
        ("송산역", "/gyeonggi/uijeongbu/station/songsan-station/"),
        ("탑석역", "/gyeonggi/uijeongbu/station/tapseok-station/"),
    ]),
    ("생활권 안내", HOME, [
        ("의정부역·중앙", "/gyeonggi/uijeongbu/area/uijeongbu-station-jungang/"),
        ("회룡·호원", "/gyeonggi/uijeongbu/area/hoeryong-howon/"),
        ("신곡·동오", "/gyeonggi/uijeongbu/area/singok-dongo/"),
        ("금오·경기도청북부청사", "/gyeonggi/uijeongbu/area/geumo-northern-office/"),
        ("민락·낙양", "/gyeonggi/uijeongbu/area/minrak-nagyang/"),
        ("고산·산곡", "/gyeonggi/uijeongbu/area/gosan-sangok/"),
        ("탑석·송산", "/gyeonggi/uijeongbu/area/tapseok-songsan/"),
    ]),
    ("예약 안내", "/reservation/", []),
    ("이용 전 확인사항", "/check/", []),
    ("홈타이 이용 가이드", "/guide/", []),
    ("고객센터", "/support/", [
        ("개인정보처리방침", "/support/privacy/"),
    ]),
]
