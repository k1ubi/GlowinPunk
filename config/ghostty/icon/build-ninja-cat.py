def mirror(c): return f'<g transform="matrix(-1 0 0 1 1024 0)">{c}</g>'
def both(c): return c + mirror(c)

import random
random.seed(7)
# neon skyline
bld=[]; x=100
while x<924:
    w=random.choice([36,44,52,60,68]); h=random.choice([60,84,110,140,96,70])
    top=924-h
    bld.append(f'<rect x="{x}" y="{top}" width="{w}" height="{h+10}" fill="url(#bldG)"/>')
    bld.append(f'<rect x="{x}" y="{top}" width="{w}" height="3" fill="#ff1744" opacity="0.55"/>')
    for wy in range(top+10, 924, 16):
        for wx in range(x+7, x+w-6, 12):
            if random.random()<0.22:
                col=random.choice(['#2ff3ff','#ff1744','#2ff3ff','#ff4d6d'])
                bld.append(f'<rect x="{wx}" y="{wy}" width="5" height="7" fill="{col}" opacity="0.85"/>')
    x+=w+random.choice([0,2,4])
skyline=''.join(bld)

head = ("M512 330 C420 330 332 380 310 470 C296 530 300 600 330 660 C360 720 430 770 512 772 "
        "C594 770 664 720 694 660 C724 600 728 530 714 470 C692 380 604 330 512 330 Z")

ear = '''
<path d="M326 448 L296 232 C352 258 412 298 456 348 Z" fill="url(#furG)" stroke="url(#rimL)" stroke-width="7" stroke-linejoin="round"/>
<path d="M340 410 L322 292 C356 314 392 338 420 364 Z" fill="url(#earIn)"/>
<path d="M300 250 L296 232 L318 242" fill="none" stroke="#2ff3ff" stroke-width="4" stroke-linecap="round"/>
'''
eye = '''
<path d="M346 534 C394 514 458 530 498 574 C450 588 384 580 346 534 Z" fill="url(#eyeG)" stroke="#06101a" stroke-width="3"/>
<path d="M346 534 C394 514 458 530 498 574" fill="none" stroke="#0a0a14" stroke-width="7" stroke-linecap="round"/>
<ellipse cx="438" cy="556" rx="6.5" ry="17" fill="#06101a" transform="rotate(-14 438 556)"/>
<circle cx="424" cy="546" r="4" fill="#ffffff" opacity="0.95"/>
'''
whisk = '''
<g fill="none" stroke="#2ff3ff" stroke-width="4" stroke-linecap="round">
  <path d="M318 598 L176 566"/><path d="M314 628 L166 630"/><path d="M322 658 L184 698"/>
</g>
'''
brow = '<path d="M338 506 L474 536" stroke="#2a2d4a" stroke-width="9" stroke-linecap="round" fill="none"/>'

particles=''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" opacity="{o}"/>' for x,y,r,c,o in [
 (190,250,2.6,'#ff4d6d',.7),(250,190,2,'#2ff3ff',.7),(160,380,2,'#2ff3ff',.6),(850,400,2.4,'#ff4d6d',.7),
 (780,190,2,'#ff4d6d',.6),(180,520,2.2,'#ff1744',.7),(870,500,2,'#2ff3ff',.6),(330,150,2,'#ff4d6d',.6)])

svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="80%">
      <stop offset="0" stop-color="#2a0a24"/><stop offset="0.55" stop-color="#0f0414"/><stop offset="1" stop-color="#040208"/>
    </radialGradient>
    <linearGradient id="moon" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ff5a78"/><stop offset="0.55" stop-color="#ff1744"/><stop offset="1" stop-color="#9b0a3a"/>
    </linearGradient>
    <linearGradient id="furG" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#262a44"/><stop offset="1" stop-color="#090a14"/>
    </linearGradient>
    <linearGradient id="rimL" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#2ff3ff"/><stop offset="0.5" stop-color="#7a6bff"/><stop offset="1" stop-color="#ff2a62"/>
    </linearGradient>
    <linearGradient id="rimH" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#2ff3ff"/><stop offset="0.5" stop-color="#8a5bff"/><stop offset="1" stop-color="#ff2a62"/>
    </linearGradient>
    <linearGradient id="earIn" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ff4d6d"/><stop offset="1" stop-color="#5a0818"/>
    </linearGradient>
    <linearGradient id="bldG" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#2c1450"/><stop offset="1" stop-color="#10061f"/>
    </linearGradient>
    <linearGradient id="band" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ff5a78"/><stop offset="1" stop-color="#c4002b"/>
    </linearGradient>
    <linearGradient id="plate" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#3a3f66"/><stop offset="1" stop-color="#12142a"/>
    </linearGradient>
    <linearGradient id="mask" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#242850"/><stop offset="1" stop-color="#0a0b1c"/>
    </linearGradient>
    <radialGradient id="eyeG" cx="50%" cy="50%" r="60%">
      <stop offset="0" stop-color="#e6fdff"/><stop offset="0.6" stop-color="#4ff5ff"/><stop offset="1" stop-color="#16b8d4"/>
    </radialGradient>
    <linearGradient id="steel" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#8fa0c8"/>
    </linearGradient>
    <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="9" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="soft" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="4.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="bloom" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="30"/></filter>
    <clipPath id="tile"><rect x="100" y="100" width="824" height="824" rx="185"/></clipPath>
  </defs>

  <rect x="100" y="100" width="824" height="824" rx="185" fill="url(#bg)"/>
  <g clip-path="url(#tile)">
    <circle cx="512" cy="470" r="270" fill="#ff1744" opacity="0.5" filter="url(#bloom)"/>
    <circle cx="512" cy="470" r="244" fill="url(#moon)" opacity="0.95"/>
    <circle cx="512" cy="470" r="300" fill="none" stroke="#2ff3ff" stroke-width="2" opacity="0.3"/>
    {particles}
    <!-- skyline -->
    <g>{skyline}</g>
    <rect x="100" y="860" width="824" height="64" fill="#ff1744" opacity="0.10"/>
    <!-- shuriken -->
    <g transform="translate(790 300) rotate(18)" filter="url(#glow)">
      <path d="M0 -52 L15 -15 L52 0 L15 15 L0 52 L-15 15 L-52 0 L-15 -15 Z" fill="url(#steel)" stroke="#2ff3ff" stroke-width="3" stroke-linejoin="round"/>
      <circle r="8" fill="#0f0414"/>
    </g>
    <g stroke="#2ff3ff" stroke-linecap="round" opacity="0.55">
      <path d="M850 290L912 282" stroke-width="3"/><path d="M846 312L900 312" stroke-width="2"/><path d="M842 270L890 256" stroke-width="2"/>
    </g>
  </g>

  <rect x="112" y="112" width="800" height="800" rx="173" fill="none" stroke="#ff1744" stroke-width="7" filter="url(#soft)"/>
  <rect x="130" y="130" width="764" height="764" rx="158" fill="none" stroke="#2ff3ff" stroke-width="1.8" opacity="0.35"/>

  <!-- headband tails -->
  <g filter="url(#soft)">
    <path d="M714 450 C790 436 856 470 898 546 L864 552 C832 504 778 490 716 492 Z" fill="url(#band)" stroke="#ff1744" stroke-width="3" stroke-linejoin="round"/>
    <path d="M712 468 C790 474 852 526 878 612 L844 604 C822 548 776 514 714 504 Z" fill="url(#band)" stroke="#ff1744" stroke-width="3" stroke-linejoin="round"/>
  </g>

  <!-- ears -->
  <g filter="url(#soft)">{both(ear)}</g>
  <g fill="none" stroke="#2ff3ff" stroke-width="4" stroke-linecap="round" filter="url(#soft)">
    <circle cx="311" cy="338" r="8"/>
  </g>

  <!-- head -->
  <g filter="url(#glow)"><path d="{head}" fill="url(#furG)" stroke="url(#rimH)" stroke-width="8" stroke-linejoin="round"/></g>

  <!-- headband -->
  <g filter="url(#soft)">
    <path d="M308 442 C420 420 604 420 716 442 L714 488 C604 466 420 466 310 488 Z" fill="url(#band)" stroke="#ff1744" stroke-width="3" stroke-linejoin="round"/>
  </g>
  <!-- plate with terminal prompt -->
  <g filter="url(#soft)">
    <rect x="452" y="418" width="120" height="58" rx="10" fill="url(#plate)" stroke="#cfd8ff" stroke-width="3"/>
    <path d="M486 436 L508 447 L486 458" fill="none" stroke="#2ff3ff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M520 460 L546 460" stroke="#2ff3ff" stroke-width="7" stroke-linecap="round"/>
  </g>

  <!-- brows + eyes -->
  {both(brow)}
  <g filter="url(#glow)">{both(eye)}</g>

  <!-- nose -->
  <path d="M500 618 L524 618 L512 636 Z" fill="#ff4d6d"/>

  <!-- ninja mask -->
  <path d="M302 632 C380 606 444 620 512 638 C580 620 644 606 722 632 C730 692 692 742 644 756 C604 780 562 794 512 796 C462 794 420 780 380 756 C332 742 294 692 302 632 Z"
        fill="url(#mask)" stroke="#ff1744" stroke-width="3" stroke-opacity="0.7" stroke-linejoin="round"/>
  <path d="M302 632 C380 606 444 620 512 638 C580 620 644 606 722 632" fill="none" stroke="#ff1744" stroke-width="5" stroke-linecap="round" filter="url(#soft)"/>
  <g fill="none" stroke="#2ff3ff" stroke-width="2.5" stroke-linecap="round" opacity="0.6">
    <path d="M388 690 L512 722 L636 690"/><path d="M512 722 L512 790"/>
    <path d="M356 660 L398 676"/><path d="M668 660 L626 676"/>
  </g>
  <g fill="#2ff3ff" filter="url(#soft)">
    <rect x="470" y="744" width="22" height="6" rx="3"/><rect x="532" y="744" width="22" height="6" rx="3"/>
  </g>

  <!-- whiskers -->
  <g filter="url(#soft)">{both(whisk)}</g>
</svg>
'''
open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'ninja-cat.svg'),'w').write(svg)
