import json
from .site import BRAND, BASE_URL, PHONE, HOME

_BASE = BASE_URL.rstrip("/")

# 메타 설명 (80자 이내)
DESC = "의정부 출장마사지·홈타이 예약 전 의정부역, 회룡역, 민락동, 신곡동, 호원동, 고산동 생활권을 확인하세요."

# 자주 묻는 질문 (FAQ 스키마 / 지시서 §9 Section 6)
_FAQ = [
    ("의정부는 구별 페이지를 만들어야 하나요?",
     "의정부시는 행정구가 없는 도시이므로 구별 페이지를 만들지 않습니다. 의정부 홈, 대표 지역, 역세권, 생활권 구조로 안내하는 것이 검색 의도에 맞습니다."),

    ("의정부역과 의정부동 페이지는 어떻게 다른가요?",
     "의정부동 페이지는 원도심과 지역 생활권을 기준으로, 의정부역 페이지는 역세권과 이동 동선을 기준으로 안내합니다. 같은 본문을 사용하지 않고 역할을 분리합니다."),

    ("회룡역은 1호선과 경전철을 따로 나눠야 하나요?",
     "나누지 않습니다. 회룡역은 1호선과 의정부경전철 환승역이지만 역명 기준 한 페이지에서 호원동·발곡역·망월사역 생활권을 함께 안내합니다."),

    ("예약 전에 꼭 확인해야 할 사항은 무엇인가요?",
     "방문 가능 주소, 예약 가능 시간, 추가 이동비 여부, 건물 출입 방식, 결제 방식, 예약 변경 기준을 먼저 확인하는 것이 좋습니다."),

    ("민락동·낙양동·고산동은 어떻게 구분되나요?",
     "민락동은 민락2지구와 송산·탑석 생활권, 낙양동은 민락과 고산 사이 생활권, 고산동은 고산지구 신규 주거 생활권을 기준으로 서로 다른 정보로 안내합니다."),

    ("외곽 지역도 방문이 가능한가요?",
     "녹양동, 자일동, 산곡동 같은 외곽 생활권도 차량 이동 기준으로 방문 가능 여부를 확인할 수 있습니다. 추가 이동비 발생 여부를 예약 시 먼저 확인하세요."),
]

_faq_schema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "@id": f"#faq-{i+1}",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a},
        }
        for i, (q, a) in enumerate(_FAQ)
    ],
}
_faq_schema_str = json.dumps(_faq_schema, ensure_ascii=False, indent=2)

# 사업자/서비스 스키마 (실제 오프라인 주소가 없는 방문형이므로 LocalBusiness 미사용)
_org_schema = {
    "@context": "https://schema.org",
    "@type": "HealthAndBeautyBusiness",
    "name": BRAND,
    "telephone": PHONE,
    "url": _BASE + HOME,
    "image": _BASE + "/assets/og-image.png",
    "description": "의정부시 출장마사지·홈타이 방문 가능 지역 안내",
    "areaServed": {"@type": "AdministrativeArea", "name": "경기도 의정부시"},
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.8",
        "reviewCount": "327",
        "bestRating": "5",
        "worstRating": "1",
    },
    "openingHoursSpecification": {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday",
                      "Friday", "Saturday", "Sunday"],
        "opens": "00:00",
        "closes": "23:59",
    },
}
_org_schema_str = json.dumps(_org_schema, ensure_ascii=False, indent=2)

# 선호 썸네일 지정 (ImageObject) — 지시서 §2 ImageObject 스키마
_image_schema = {
    "@context": "https://schema.org",
    "@type": "ImageObject",
    "contentUrl": _BASE + "/assets/og-image.png",
    "url": _BASE + "/assets/og-image.png",
    "width": 1200,
    "height": 630,
    "caption": "의정부 출장마사지·홈타이 지역별 안내",
}
_image_schema_str = json.dumps(_image_schema, ensure_ascii=False, indent=2)

_breadcrumb_schema = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "의정부 출장마사지",
         "item": _BASE + "/"},
    ],
}
_breadcrumb_schema_str = json.dumps(_breadcrumb_schema, ensure_ascii=False, indent=2)

_EXTRA_HEAD = f"""<script type="application/ld+json">
{_org_schema_str}
</script>
<script type="application/ld+json">
{_breadcrumb_schema_str}
</script>
<script type="application/ld+json">
{_image_schema_str}
</script>
<script type="application/ld+json">
{_faq_schema_str}
</script>"""

_HERO = """<div class="hero">
  <div class="hero-content">
    <div class="hero-badge">의정부시 전지역 방문 관리</div>
    <h1 class="hero-title">의정부 출장마사지<br><span class="hero-accent">홈타이</span><br>지역별 예약 안내</h1>
    <p class="hero-lead">의정부역, 회룡역, 민락동, 신곡동, 호원동, 고산동, 금오동, 가능동 생활권별 방문 가능 지역과 예약 전 확인사항을 안내합니다.</p>
    <div class="rating-badge rating-badge-hero" aria-label="이용 만족도 평점">
      <span class="rating-stars" aria-hidden="true">★★★★★</span>
      <span class="rating-score"><strong>4.8</strong><span class="rating-out">/ 5</span></span>
      <span class="rating-count">의정부 방문 관리 이용 만족도 후기 327건 기준</span>
    </div>
    <div class="hero-cta">
      <a href="#areas" class="btn btn-primary">지역별 안내 보기</a>
      <a href="#stations" class="btn btn-secondary">가까운 역 찾기</a>
      <a href="/reservation/" class="btn btn-secondary">예약 안내 보기</a>
      <a href="/check/" class="btn btn-secondary">이용 전 확인사항</a>
    </div>
  </div>
  <div class="hero-stats">
    <div class="stat">
      <div class="stat-number">16</div>
      <div class="stat-label">지역 페이지</div>
    </div>
    <div class="stat">
      <div class="stat-number">20</div>
      <div class="stat-label">역세권 안내</div>
    </div>
    <div class="stat">
      <div class="stat-number">13</div>
      <div class="stat-label">생활권 안내</div>
    </div>
    <div class="stat">
      <div class="stat-number">24H</div>
      <div class="stat-label">상담 가능</div>
    </div>
  </div>
</div>"""

PAGE = {
    "path": "",
    "title": "의정부 출장마사지｜의정부역·민락·신곡·호원 홈타이 지역 안내",
    "desc": DESC,
    "h1": "의정부 출장마사지·홈타이 지역별 예약 안내",
    "hero": _HERO,
    "breadcrumb": [],
    "extra_head": _EXTRA_HEAD,
    "body": """
<section id="criteria">
  <h2>의정부에서 출장마사지를 찾을 때 먼저 확인할 기준</h2>
  <p>의정부 출장마사지와 의정부 홈타이를 예약하기 전에는, 자신의 위치가 의정부시 안에서 어느 생활권에 속하는지부터 확인하는 것이 가장 중요합니다. 의정부시는 행정구가 따로 없는 도시이지만, 1호선과 의정부경전철이 도시를 가로지르며 생활권 차이가 뚜렷하게 나뉩니다. 같은 의정부라도 원도심 상권, 환승 생활권, 시청·행정 생활권, 동부 신도시형 주거지, 외곽 차량 이동권은 방문 동선과 예약 기준이 서로 다릅니다.</p>
  <p>의정부역과 <a href="/gyeonggi/uijeongbu/station/uijeongbu-jungang-station/">의정부중앙역</a> 주변은 중앙로를 낀 원도심·상권 중심 생활권입니다. <a href="/gyeonggi/uijeongbu/station/hoeryong-station/">회룡역</a>과 <a href="/gyeonggi/uijeongbu/howon-dong/">호원동</a>은 1호선과 경전철이 만나는 환승 생활권으로, 망월사역·발곡역·범골역과 이어집니다. <a href="/gyeonggi/uijeongbu/singok-dong/">신곡동</a>과 <a href="/gyeonggi/uijeongbu/geumo-dong/">금오동</a>은 의정부시청, 경기도청북부청사, 동오역, 새말역과 연결되는 행정·주거 생활권입니다.</p>
  <p>동부의 <a href="/gyeonggi/uijeongbu/minrak-dong/">민락동</a>, <a href="/gyeonggi/uijeongbu/nagyang-dong/">낙양동</a>, <a href="/gyeonggi/uijeongbu/gosan-dong/">고산동</a>은 민락2지구와 고산지구를 중심으로 한 신도시형 주거 생활권이라 검색 의도가 다르고, <a href="/gyeonggi/uijeongbu/station/tapseok-station/">탑석역</a>이 이 일대를 연결하는 거점 역할을 합니다. 반면 <a href="/gyeonggi/uijeongbu/nogyang-dong/">녹양동</a>, <a href="/gyeonggi/uijeongbu/jail-dong/">자일동</a>, <a href="/gyeonggi/uijeongbu/sangok-dong/">산곡동</a> 같은 외곽 생활권은 차량 이동 기준과 추가 이동비 확인이 특히 중요합니다.</p>
  <p>의정부 전역으로 방문이 가능하며, 자택·숙소·오피스텔 등 다양한 장소에 대응합니다. 예약 전에 정확한 방문 주소, 가장 가까운 지하철·경전철역, 기본 이동권 범위, 추가 이동비 여부를 미리 확인하면 예약 과정이 한결 수월해집니다. 자세한 항목은 <a href="/check/">이용 전 확인사항</a>에서 확인하세요.</p>
</section>

<section id="areas">
  <h2>의정부 대표 지역별 방문 가능 지역 안내</h2>
  <div class="card-grid">
    <a href="/gyeonggi/uijeongbu/uijeongbu-dong/" class="card">
      <h3>의정부동</h3>
      <p>의정부역, 의정부중앙역, 경전철의정부역 인접 원도심 생활권</p>
      <span class="card-arrow">→</span>
    </a>
    <a href="/gyeonggi/uijeongbu/howon-dong/" class="card">
      <h3>호원동</h3>
      <p>회룡역, 망월사역, 발곡역, 범골역 인접 생활권</p>
      <span class="card-arrow">→</span>
    </a>
    <a href="/gyeonggi/uijeongbu/jangam-dong/" class="card">
      <h3>장암동</h3>
      <p>장암역, 발곡역, 호원동 인접 생활권</p>
      <span class="card-arrow">→</span>
    </a>
    <a href="/gyeonggi/uijeongbu/singok-dong/" class="card">
      <h3>신곡동</h3>
      <p>동오역, 새말역, 의정부시청역 인접 생활권</p>
      <span class="card-arrow">→</span>
    </a>
    <a href="/gyeonggi/uijeongbu/geumo-dong/" class="card">
      <h3>금오동</h3>
      <p>경기도청북부청사역, 효자역, 자금동 인접 생활권</p>
      <span class="card-arrow">→</span>
    </a>
    <a href="/gyeonggi/uijeongbu/ganeung-dong/" class="card">
      <h3>가능동</h3>
      <p>가능역, 흥선동, 녹양동 인접 생활권</p>
      <span class="card-arrow">→</span>
    </a>
    <a href="/gyeonggi/uijeongbu/heungseon-dong/" class="card">
      <h3>흥선동</h3>
      <p>흥선역, 가능동, 의정부동 인접 생활권</p>
      <span class="card-arrow">→</span>
    </a>
    <a href="/gyeonggi/uijeongbu/nogyang-dong/" class="card">
      <h3>녹양동</h3>
      <p>녹양역, 자금동, 가능동 인접 생활권</p>
      <span class="card-arrow">→</span>
    </a>
    <a href="/gyeonggi/uijeongbu/yonghyeon-dong/" class="card">
      <h3>용현동</h3>
      <p>곤제역, 어룡역, 송산역 인접 생활권</p>
      <span class="card-arrow">→</span>
    </a>
    <a href="/gyeonggi/uijeongbu/minrak-dong/" class="card">
      <h3>민락동</h3>
      <p>송산역, 어룡역, 낙양동, 고산동 인접 생활권</p>
      <span class="card-arrow">→</span>
    </a>
    <a href="/gyeonggi/uijeongbu/nagyang-dong/" class="card">
      <h3>낙양동</h3>
      <p>민락동, 고산동, 탑석역 인접 생활권</p>
      <span class="card-arrow">→</span>
    </a>
    <a href="/gyeonggi/uijeongbu/gosan-dong/" class="card">
      <h3>고산동</h3>
      <p>고산지구, 산곡동, 민락동 인접 생활권</p>
      <span class="card-arrow">→</span>
    </a>
    <a href="/gyeonggi/uijeongbu/sangok-dong/" class="card">
      <h3>산곡동</h3>
      <p>고산동, 자일동, 외곽 차량 이동 생활권</p>
      <span class="card-arrow">→</span>
    </a>
    <a href="/gyeonggi/uijeongbu/songsan-area/" class="card">
      <h3>송산 생활권</h3>
      <p>용현동, 민락동, 낙양동, 고산동을 잇는 동부 생활권</p>
      <span class="card-arrow">→</span>
    </a>
  </div>
</section>

<section id="stations">
  <h2>의정부 주요 지하철역·경전철역별 홈타이 안내</h2>
  <p>의정부의 1호선·7호선·의정부경전철 주요 역별로 인접 지역과 예약 기준을 정리했습니다. 역세권 페이지는 역명 기준 한 페이지로만 운영하며, 환승역도 노선별로 나누지 않습니다.</p>
  <div class="card-grid">
    <a href="/gyeonggi/uijeongbu/station/uijeongbu-station/" class="card">
      <h3>의정부역</h3>
      <p>의정부동, 의정부중앙역, 경전철의정부역 인접 생활권입니다. 방문 주소와 건물 출입 가능 여부를 먼저 확인하세요.</p>
    </a>
    <a href="/gyeonggi/uijeongbu/station/hoeryong-station/" class="card">
      <h3>회룡역</h3>
      <p>호원동, 발곡역, 망월사역 인접 생활권입니다. 환승역이지만 노선별로 나누지 않고 한 페이지에서 안내합니다.</p>
    </a>
    <a href="/gyeonggi/uijeongbu/station/mangwolsa-station/" class="card">
      <h3>망월사역</h3>
      <p>호원동, 장암 인접 생활권입니다.</p>
    </a>
    <a href="/gyeonggi/uijeongbu/station/ganeung-station/" class="card">
      <h3>가능역</h3>
      <p>가능동, 흥선동, 의정부역 인접 생활권입니다.</p>
    </a>
    <a href="/gyeonggi/uijeongbu/station/nogyang-station/" class="card">
      <h3>녹양역</h3>
      <p>녹양동, 자금동, 가능동 인접 생활권입니다.</p>
    </a>
    <a href="/gyeonggi/uijeongbu/station/jangam-station/" class="card">
      <h3>장암역</h3>
      <p>장암동, 발곡역, 호원동 인접 생활권입니다.</p>
    </a>
    <a href="/gyeonggi/uijeongbu/station/uijeongbu-cityhall-station/" class="card">
      <h3>의정부시청역</h3>
      <p>신곡동, 흥선동 인접 생활권입니다.</p>
    </a>
    <a href="/gyeonggi/uijeongbu/station/uijeongbu-jungang-station/" class="card">
      <h3>의정부중앙역</h3>
      <p>의정부동, 중앙로 인접 생활권입니다.</p>
    </a>
    <a href="/gyeonggi/uijeongbu/station/dongo-station/" class="card">
      <h3>동오역</h3>
      <p>신곡동, 금오동 인접 생활권입니다.</p>
    </a>
    <a href="/gyeonggi/uijeongbu/station/gyeonggi-provincial-government-northern-office-station/" class="card">
      <h3>경기도청북부청사역</h3>
      <p>금오동, 신곡동 인접 생활권입니다.</p>
    </a>
    <a href="/gyeonggi/uijeongbu/station/songsan-station/" class="card">
      <h3>송산역</h3>
      <p>민락동, 용현동 인접 생활권입니다.</p>
    </a>
    <a href="/gyeonggi/uijeongbu/station/tapseok-station/" class="card">
      <h3>탑석역</h3>
      <p>민락동, 송산동, 고산동 인접 생활권입니다. 차량 이동 기준과 추가 이동비 여부를 확인하세요.</p>
    </a>
  </div>
</section>

<section id="lifestyle">
  <h2>의정부 생활권별 예약 기준</h2>
  <p>생활권 페이지는 지역 페이지와 역세권 페이지 사이를 잇는 중간 허브입니다. 인접한 동과 역을 묶어 방문 주소와 이동 시간을 더 정확히 확인할 수 있습니다.</p>
  <div class="card-grid">
    <a href="/gyeonggi/uijeongbu/area/uijeongbu-station-jungang/" class="card">의정부역·중앙</a>
    <a href="/gyeonggi/uijeongbu/area/hoeryong-howon/" class="card">회룡·호원</a>
    <a href="/gyeonggi/uijeongbu/area/singok-dongo/" class="card">신곡·동오</a>
    <a href="/gyeonggi/uijeongbu/area/geumo-northern-office/" class="card">금오·경기도청북부청사</a>
    <a href="/gyeonggi/uijeongbu/area/minrak-nagyang/" class="card">민락·낙양</a>
    <a href="/gyeonggi/uijeongbu/area/gosan-sangok/" class="card">고산·산곡</a>
    <a href="/gyeonggi/uijeongbu/area/tapseok-songsan/" class="card">탑석·송산</a>
  </div>
</section>

<section id="longtail">
  <h2>의정부 출장마사지·홈타이 주제별 바로가기</h2>
  <p>찾으시는 상황과 생활권에 맞춰 자주 검색되는 주제별로 안내 페이지를 정리했습니다. 동·역·생활권 안내를 함께 확인하면 방문 동선과 예약 기준을 더 빠르게 파악할 수 있습니다.</p>
  <ul class="longtail-list">
    <li><a href="/gyeonggi/uijeongbu/minrak-dong/">민락2지구 민락동 출장마사지 방문 가능 지역 확인</a></li>
    <li><a href="/gyeonggi/uijeongbu/gosan-dong/">고산지구 고산동 홈타이 신축 아파트 방문 동선</a></li>
    <li><a href="/gyeonggi/uijeongbu/station/tapseok-station/">탑석역 출장마사지 차량 이동·추가 이동비 기준</a></li>
    <li><a href="/gyeonggi/uijeongbu/station/hoeryong-station/">회룡역 환승 생활권 호원동 홈타이 예약 안내</a></li>
    <li><a href="/gyeonggi/uijeongbu/uijeongbu-dong/">의정부역·중앙로 원도심 의정부동 출장마사지 안내</a></li>
    <li><a href="/gyeonggi/uijeongbu/singok-dong/">신곡동 의정부시청 인접 생활권 홈타이 방문 안내</a></li>
    <li><a href="/gyeonggi/uijeongbu/area/geumo-northern-office/">금오동·경기도청북부청사 행정 생활권 예약 동선</a></li>
    <li><a href="/gyeonggi/uijeongbu/nogyang-dong/">녹양동·자일동 외곽 생활권 차량 방문 가능 여부</a></li>
    <li><a href="/reservation/">의정부 출장마사지 예약 방법과 예약 가능 시간 안내</a></li>
    <li><a href="/check/">방문 전 추가 이동비·건물 출입·결제 방식 확인사항</a></li>
  </ul>
</section>

<section id="check">
  <h2>의정부 홈타이 예약 전 확인사항</h2>
  <p>예약을 진행하기 전에 다음 항목을 먼저 확인하면 예약 과정이 훨씬 수월합니다. 더 자세한 내용은 <a href="/check/">이용 전 확인사항</a>과 <a href="/guide/">홈타이 이용 가이드</a>를 참고하세요.</p>
  <ul>
    <li><strong>방문 가능 주소 확인</strong> — 자택·숙소·오피스텔 등 정확한 방문 주소와 건물 유형</li>
    <li><strong>예약 가능 시간 확인</strong> — 희망 예약 시간이 가능한지 미리 확인</li>
    <li><strong>추가 이동비 여부 확인</strong> — 기본 이동권 외 추가 이동비 발생 여부</li>
    <li><strong>건물 출입 방식 확인</strong> — 공동현관, 자동문, 경비 확인 등</li>
    <li><strong>자택·숙소·오피스텔 이용 기준 확인</strong> — 서비스 제공 장소 기준</li>
    <li><strong>결제 방식 확인</strong> — 현금, 계좌이체, 카드 등 가능한 결제 수단</li>
    <li><strong>예약 변경·취소 기준 확인</strong> — 변경·취소 절차 및 기준</li>
    <li><strong>개인정보 처리 기준 확인</strong> — <a href="/support/privacy/">개인정보처리방침</a> 참조</li>
    <li><strong>불법·선정적 서비스 불가 안내</strong> — 건전한 방문 관리 서비스만 제공</li>
  </ul>
</section>

<section id="faq">
  <h2>의정부 출장마사지 자주 묻는 질문</h2>
  <dl class="faq-list">
    <dt id="faq-1">의정부는 구별 페이지를 만들어야 하나요?</dt>
    <dd>의정부시는 행정구가 없는 도시이므로 구별 페이지를 만들지 않습니다. 의정부 홈, 대표 지역, 역세권, 생활권 구조로 안내하는 것이 검색 의도에 맞습니다.</dd>

    <dt id="faq-2">의정부역과 의정부동 페이지는 어떻게 다른가요?</dt>
    <dd>의정부동 페이지는 원도심과 지역 생활권을 기준으로, 의정부역 페이지는 역세권과 이동 동선을 기준으로 안내합니다. 같은 본문을 사용하지 않고 역할을 분리합니다.</dd>

    <dt id="faq-3">회룡역은 1호선과 경전철을 따로 나눠야 하나요?</dt>
    <dd>나누지 않습니다. 회룡역은 1호선과 의정부경전철 환승역이지만 역명 기준 한 페이지에서 호원동·발곡역·망월사역 생활권을 함께 안내합니다.</dd>

    <dt id="faq-4">예약 전에 꼭 확인해야 할 사항은 무엇인가요?</dt>
    <dd>방문 가능 주소, 예약 가능 시간, 추가 이동비 여부, 건물 출입 방식, 결제 방식, 예약 변경 기준을 먼저 확인하는 것이 좋습니다.</dd>

    <dt id="faq-5">민락동·낙양동·고산동은 어떻게 구분되나요?</dt>
    <dd>민락동은 민락2지구와 송산·탑석 생활권, 낙양동은 민락과 고산 사이 생활권, 고산동은 고산지구 신규 주거 생활권을 기준으로 서로 다른 정보로 안내합니다.</dd>

    <dt id="faq-6">외곽 지역도 방문이 가능한가요?</dt>
    <dd>녹양동, 자일동, 산곡동 같은 외곽 생활권도 차량 이동 기준으로 방문 가능 여부를 확인할 수 있습니다. 추가 이동비 발생 여부를 예약 시 먼저 확인하세요.</dd>
  </dl>
</section>
"""
}
