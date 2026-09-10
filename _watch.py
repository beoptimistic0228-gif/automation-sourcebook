# -*- coding: utf-8 -*-
"""탭 아래에 「낙관이 보고 있는 것」 섹션을 만든다.
직업별 사례가 아니라 Owner가 골라 둔 시청 목록이라 카드도 가볍게 간다.
자막 원문 확인 2026-09-10.
"""
import io

p = "index.html"
s = io.open(p, encoding="utf-8").read()

# ── 1) 마크업 — 카드 그리드 바로 아래
old = """  <div class="grid" id="grid"></div>
</main>"""
new = """  <div class="grid" id="grid"></div>

  <section class="watch">
    <div class="wtop">
      <h2>👀 낙관이 보고 있는 것</h2>
      <p>직업별 사례는 아닙니다. 제가 보면서 도움이 됐던 것들을 모아 뒀습니다.
         눌러 보시고 필요 없으면 그냥 지나가셔도 됩니다.</p>
    </div>
    <div id="watch"></div>
  </section>
</main>"""
assert old in s
s = s.replace(old, new)

# ── 2) 스타일
s = s.replace("footer{border-top:3px solid var(--ink);",
""".watch{margin-top:clamp(56px,8vw,104px);border-top:3px dashed var(--ink);padding-top:clamp(32px,4vw,52px)}
.wtop h2{font-family:var(--disp);font-weight:400;font-size:clamp(24px,3.4vw,36px);margin-bottom:10px}
.wtop p{color:var(--ink-70);font-weight:500;max-width:56ch;margin-bottom:34px}
.wgroup{margin-bottom:38px}
.wgroup h3{display:inline-block;font-family:var(--sans);font-weight:700;font-size:16.5px;
  background:var(--lemon);border:3px solid var(--ink);border-radius:999px;padding:6px 16px;
  box-shadow:3px 3px 0 var(--ink);margin-bottom:20px}
.wlist{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:22px}
.wcard{display:flex;flex-direction:column;background:#fff;border:3px solid var(--ink);border-radius:20px;
  overflow:hidden;text-decoration:none;color:inherit;box-shadow:var(--shadow);
  transition:transform .16s ease,box-shadow .16s ease}
.wcard:hover{transform:translate(-3px,-3px);box-shadow:var(--shadow-lg)}
.wcard:focus-visible{outline:4px solid var(--coral);outline-offset:3px}
.wthumb{position:relative;aspect-ratio:16/9;border-bottom:3px solid var(--ink);background:var(--cream-2);overflow:hidden}
.wthumb img{width:100%;height:100%;object-fit:cover;display:block}
.wdur{position:absolute;right:9px;bottom:9px;background:var(--ink);color:var(--cream);
  border-radius:999px;padding:3px 11px;font-size:12.5px;font-weight:700}
.wdur.long{background:var(--coral);border:2px solid var(--ink)}
.wbody{padding:16px 18px 18px;display:flex;flex-direction:column;gap:9px;flex:1}
.wbody h4{font-size:17px;font-weight:700;line-height:1.45}
.wmeta{font-size:13px;color:var(--ink-70);font-weight:500}
.wwhy{font-size:15.5px;color:var(--ink);font-weight:500;flex:1}
.wnote{font-size:13px;font-weight:700;border:2.5px solid var(--ink);border-radius:999px;
  padding:3px 11px;background:#fff;align-self:flex-start}
@media(max-width:640px){.wlist{grid-template-columns:1fr}}
footer{border-top:3px solid var(--ink);""")

# ── 3) 데이터와 렌더러
s = s.replace("document.getElementById('dlgClose').onclick", r'''/* 낙관이 고른 시청 목록 — 사례집이 아니라 참고 목록이라 상세를 만들지 않고 원본으로 바로 보낸다 */
var WATCH = [
 {g:"🎁 가져다 쓰는 것", items:[
  {id:"9hAcDsqHlR4", t:"네이버 블로그 자동화, 돈 내고 쓰지 마세요 — Codex 프로그램 소스 무료 공개", ch:"복사장", d:"2026-08-23", dur:"45분",
   why:"완성된 프로그램을 통째로 공개했습니다. 따로 결제하는 방식이 아니라 코덱스 구독량으로 돌아가고, 「고쳐 쓰면서 연습하라」는 게 만든 사람의 뜻입니다."},
  {id:"a-oG2FJwTz0", t:"보조금24 데이터로 내 혜택만 걸러주는 웹앱 만들어봅시다", ch:"방구석컴퍼니", d:"2026-09-02", dur:"15분",
   why:"공공 데이터를 받아 화면으로 만들고 인터넷에 올리기까지가 한 벌로 들어 있습니다. 결과가 엉뚱하게 나오던 함정 세 개를 찾아 고치는 장면이 특히 볼 만합니다."}]},
 {g:"🔧 만드는 법", items:[
  {id:"v2C9qRgTzT0", t:"하루 30분, AI로 인스타그램 운영한 방법", ch:"온크트리", d:"2026-08-17", dur:"7분",
   why:"기획은 코덱스에, 손은 클로드에 맡기는 분업이 핵심입니다. 사람이 쓰는 디자인 도구를 그대로 조작하게 해서 「AI 티」를 없앴습니다."},
  {id:"bB2PyjK7QZE", t:"클로드로 쇼핑 쇼츠 자동화 — 제품 링크 하나로 AI 쇼츠 완성", ch:"홍아린 AI", d:"2026-08-25", dur:"16분", note:"협찬 고지 있음",
   why:"컷마다 얼굴과 제품이 바뀌는 문제를, 인물과 제품을 먼저 고정해 두고 푸는 방법입니다."},
  {id:"OPFMs1-WoKE", t:"클로드 영상 자동화 3탄 — 모션그래픽", ch:"데키랩", d:"2026-07-29", dur:"12분",
   why:"전문 편집 도구 없이 말로만 모션그래픽을 만듭니다. 여러 개를 만들 땐 한꺼번에 나눠 시키라는 팁이 있습니다."},
  {id:"sozxBiyc3qQ", t:"평생 써먹는 바이브코딩 자동화 대시보드 — 설계부터 구축까지", ch:"양실장의 바이브코딩대학", d:"2026-08-20", dur:"2시간 35분", long:true,
   why:"긴 강의입니다. 「대시보드는 데모까지는 빨리 나오고 그 뒤부터 어려워진다」는 지적이 이 영상의 값입니다. 시간을 비우고 보십시오."}]},
 {g:"🧭 보는 눈", items:[
  {id:"QrQRIg5EqPc", t:"AI로 만든 PPT, 그대로 쓰면 티 납니다 — 이 기준으로 수정하세요", ch:"헤이디_일잘러의 업무스킬", d:"2026-07-31", dur:"14분",
   why:"고치는 기준 두 가지를 줍니다 — 강조할 곳이 강조됐는가, 데이터가 한눈에 들어오는가. 만드는 법이 아니라 판단하는 법이라 오래 씁니다."}]}
];

(function renderWatch(){
  var box = document.getElementById('watch');
  WATCH.forEach(function(g){
    var wrap = document.createElement('div');
    wrap.className = 'wgroup';
    wrap.innerHTML = '<h3>' + g.g + '</h3><div class="wlist">' +
      g.items.map(function(v){
        return '<a class="wcard" href="https://www.youtube.com/watch?v=' + v.id + '" target="_blank" rel="noopener noreferrer">' +
          '<div class="wthumb"><img src="https://img.youtube.com/vi/' + v.id + '/hqdefault.jpg" alt="" loading="lazy" ' +
            'referrerpolicy="no-referrer" onerror="this.remove()">' +
            '<span class="wdur' + (v.long ? ' long' : '') + '">' + v.dur + '</span></div>' +
          '<div class="wbody"><h4>' + v.t + '</h4>' +
            '<div class="wmeta">' + v.ch + ' · ' + v.d + (isStale(v.d) ? ' ⏳' : '') + '</div>' +
            (v.note ? '<span class="wnote">⚠️ ' + v.note + '</span>' : '') +
            '<div class="wwhy">' + v.why + '</div></div></a>';
      }).join('') + '</div>';
    box.appendChild(wrap);
  });
})();

document.getElementById('dlgClose').onclick''', 1)

io.open(p, "w", encoding="utf-8").write(s)
assert s.count("renderWatch") == 1
assert s.count('id:"') == 7
print("watch section added — 영상", s.count('id:"'), "편")
