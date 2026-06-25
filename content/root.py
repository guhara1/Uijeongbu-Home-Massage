# 루트 페이지 (index.html) — 의정부 홈으로 이동

from .site import HOME

PAGE = {
    "path": "",  # 저장소 루트
    "title": "의정부 출장마사지｜의정부역·민락·신곡·호원 홈타이 지역 안내",
    "desc": "의정부 출장마사지·홈타이 예약 전 의정부역, 회룡역, 민락동, 신곡동, 호원동 생활권을 확인하세요.",
    "h1": "의정부 출장마사지",
    "breadcrumb": [],
    "body": (
        f'<meta http-equiv="refresh" content="0;url={HOME}" />'
        f'<p>의정부 출장마사지 안내 페이지로 이동합니다. 자동으로 이동하지 않으면 '
        f'<a href="{HOME}">여기를 클릭</a>하세요.</p>'
    ),
    "noindex": True,  # 리다이렉트 페이지는 색인 제외
}
