# Builds oni-pretty.svg. Left-side parts are mirrored automatically for exact symmetry.
def mirror(c): return f'<g transform="matrix(-1 0 0 1 1024 0)">{c}</g>'
def both(c): return c + mirror(c)

mane = '''
<path d="M318 470 L196 396 L262 482 L150 486 L256 548 L170 620 L282 600 L196 706 L318 650 Z"
      fill="#0c0206" stroke="#ff1744" stroke-width="3.5" stroke-linejoin="round" stroke-opacity="0.75"/>
<path d="M330 420 L226 320 L290 404 L196 372" fill="none" stroke="#ff1744" stroke-width="3" stroke-opacity="0.5" stroke-linecap="round"/>
'''
horn = '''
<path d="M376 428 C298 384 252 302 284 214 C294 186 314 164 344 140 C326 190 324 236 352 284 C386 342 432 372 484 394 Z" fill="url(#hornG)" stroke="#ff2a52" stroke-width="6" stroke-linejoin="round"/>
<path d="M376 428 C304 384 262 306 290 222 C298 198 314 178 334 158" fill="none" stroke="#ffd0d8" stroke-opacity="0.55" stroke-width="3" stroke-linecap="round"/>
<g fill="none" stroke="#ff1744" stroke-width="5" stroke-linecap="round" stroke-opacity="0.85">
  <path d="M334 396 C356 384 388 386 416 402"/>
  <path d="M310 346 C334 334 364 338 390 354"/>
  <path d="M300 292 C320 282 344 286 364 300"/>
</g>
<circle cx="342" cy="144" r="7" fill="#ffffff" opacity="0.9"/>
'''
brow = '''
<path d="M292 424 C380 440 454 494 510 592 C448 558 376 540 300 514 Z" fill="url(#browG)" stroke="#ff4d6d" stroke-width="3" stroke-linejoin="round"/>
'''
eye = '''
<path d="M340 580 C392 572 458 592 502 624 C454 636 384 626 340 580 Z" fill="url(#eyeG)" stroke="#2ff3ff" stroke-width="3"/>
<path d="M340 580 C392 572 458 592 502 624" fill="none" stroke="#ff1744" stroke-width="5" stroke-linecap="round"/>
<ellipse cx="442" cy="606" rx="6.5" ry="16" fill="#ff1744" transform="rotate(-8 442 606)"/>
<circle cx="428" cy="600" r="3.6" fill="#ffffff" opacity="0.9"/>
'''
cheek = '''
<g fill="none" stroke="#2ff3ff" stroke-linecap="round" stroke-opacity="0.9">
  <path d="M322 640 C326 668 340 692 360 712" stroke-width="4"/>
  <path d="M338 626 C344 652 358 676 376 694" stroke-width="3" stroke-opacity="0.6"/>
</g>
'''
fangs = '''
<g fill="url(#toothG)">
  <path d="M358 722 L390 724 L372 788 Z"/>
  <path d="M400 732 L434 736 L415 806 Z"/>
  <path d="M452 739 L484 741 L467 796 Z"/>
</g>
<g fill="url(#toothG)" opacity="0.95">
  <path d="M432 828 L466 828 L449 796 Z"/>
</g>
'''
tusk = '''
<path d="M372 770 C342 728 334 676 350 622 C390 656 412 702 414 752 Z" fill="url(#toothG)" stroke="#2ff3ff" stroke-width="4" stroke-linejoin="round"/>
'''
drip = '''
<path d="M415 806 Q 409 832 415 850 Q 423 832 415 806 Z" fill="#ff1744"/>
'''

particles = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" opacity="{o}"/>' for x,y,r,c,o in [
 (190,300,3,'#ff4d6d',.7),(230,230,2.2,'#2ff3ff',.7),(170,420,2,'#ff1744',.8),(150,560,2.6,'#ff4d6d',.6),
 (840,300,3,'#ff4d6d',.7),(790,230,2.2,'#2ff3ff',.7),(860,430,2,'#ff1744',.8),(880,580,2.6,'#ff4d6d',.6),
 (230,800,2.4,'#ff1744',.7),(800,820,2.4,'#2ff3ff',.6),(180,700,2,'#2ff3ff',.5),(850,720,2,'#ff4d6d',.7),
 (330,140,2,'#ff4d6d',.6),(700,150,2,'#ff4d6d',.6)])

face_d = ("M512 356 C452 350 392 366 350 404 C312 438 292 488 292 540 C292 600 312 650 346 696 "
          "C372 736 396 770 424 812 L512 868 L600 812 "
          "C628 770 652 736 678 696 C712 650 732 600 732 540 C732 488 712 438 674 404 C632 366 572 350 512 356 Z")

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <defs>
    <radialGradient id="bg" cx="50%" cy="46%" r="75%">
      <stop offset="0" stop-color="#3d0814"/><stop offset="0.55" stop-color="#14030a"/><stop offset="1" stop-color="#050102"/>
    </radialGradient>
    <linearGradient id="sun" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ff5a3c"/><stop offset="0.5" stop-color="#ff1744"/><stop offset="1" stop-color="#8a0a24"/>
    </linearGradient>
    <linearGradient id="face" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#40081a"/><stop offset="0.55" stop-color="#1c0409"/><stop offset="1" stop-color="#0a0204"/>
    </linearGradient>
    <radialGradient id="foreheadLight" cx="50%" cy="22%" r="55%">
      <stop offset="0" stop-color="#ff1744" stop-opacity="0.38"/><stop offset="1" stop-color="#ff1744" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="rim" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ff7a93"/><stop offset="0.5" stop-color="#ff1744"/><stop offset="1" stop-color="#c4002b"/>
    </linearGradient>
    <linearGradient id="hornG" x1="0" y1="1" x2="0" y2="0">
      <stop offset="0" stop-color="#2a0510"/><stop offset="0.6" stop-color="#7a0f26"/><stop offset="1" stop-color="#ff3a5e"/>
    </linearGradient>
    <linearGradient id="browG" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#ff5a78"/><stop offset="1" stop-color="#ff1744"/>
    </linearGradient>
    <radialGradient id="eyeG" cx="50%" cy="50%" r="60%">
      <stop offset="0" stop-color="#e6fdff"/><stop offset="0.6" stop-color="#4ff5ff"/><stop offset="1" stop-color="#16b8d4"/>
    </radialGradient>
    <linearGradient id="toothG" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#ffc2cf"/>
    </linearGradient>
    <linearGradient id="mouthG" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#05010 2"/><stop offset="1" stop-color="#5a0818"/>
    </linearGradient>
    <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="10" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="soft" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="4.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="bloom" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="28"/></filter>
    <clipPath id="tile"><rect x="100" y="100" width="824" height="824" rx="185"/></clipPath>
  </defs>

  <rect x="100" y="100" width="824" height="824" rx="185" fill="url(#bg)"/>
  <g clip-path="url(#tile)">
    <!-- halo: soft bloom + disc + ring -->
    <circle cx="512" cy="480" r="260" fill="#ff1744" opacity="0.55" filter="url(#bloom)"/>
    <circle cx="512" cy="480" r="236" fill="url(#sun)" opacity="0.92"/>
    <g fill="#14030a" opacity="0.9">
      <rect x="250" y="352" width="524" height="5"/><rect x="250" y="388" width="524" height="8"/>
      <rect x="250" y="428" width="524" height="11"/><rect x="250" y="474" width="524" height="14"/>
    </g>
    <circle cx="512" cy="480" r="290" fill="none" stroke="#ff1744" stroke-width="3" stroke-dasharray="3 12" opacity="0.7"/>
    <circle cx="512" cy="480" r="332" fill="none" stroke="#2ff3ff" stroke-width="2" opacity="0.28"/>
    <!-- low floor glow -->
    <rect x="100" y="800" width="824" height="124" fill="#ff1744" opacity="0.12"/>
    <g stroke="#ff1744" stroke-opacity="0.18" stroke-width="2">
      <path d="M100 842H924M100 872H924M100 908H924"/>
      <path d="M512 820L512 924M400 820L300 924M624 820L724 924M290 820L120 924M734 820L904 924"/>
    </g>
    {particles}
  </g>

  <!-- double border -->
  <rect x="112" y="112" width="800" height="800" rx="173" fill="none" stroke="#ff1744" stroke-width="7" filter="url(#soft)"/>
  <rect x="130" y="130" width="764" height="764" rx="158" fill="none" stroke="#2ff3ff" stroke-width="1.8" opacity="0.35"/>

  <!-- mane -->
  {both(mane)}

  <!-- horns -->
  <g filter="url(#glow)">{both(horn)}</g>

  <!-- face -->
  <g filter="url(#glow)"><path d="{face_d}" fill="url(#face)" stroke="url(#rim)" stroke-width="9" stroke-linejoin="round"/></g>
  <path d="{face_d}" fill="url(#foreheadLight)"/>
  <!-- cheek shading -->
  <path d="M312 640 C340 724 398 780 470 828 L430 806 C398 764 372 732 346 696 Z" fill="#000" opacity="0.28"/>
  <path d="M712 640 C684 724 626 780 554 828 L594 806 C626 764 652 732 678 696 Z" fill="#000" opacity="0.28"/>

  <!-- forehead jewel + brow lines -->
  <g filter="url(#glow)"><path d="M512 376 L530 420 L512 468 L494 420 Z" fill="#2ff3ff"/></g>
  <path d="M512 376 L512 360 M512 468 L512 500" stroke="#ff1744" stroke-width="5" stroke-linecap="round"/>
  <g fill="none" stroke="#ff4d6d" stroke-width="3" stroke-linecap="round" opacity="0.7">
    <path d="M470 402 C484 392 496 392 502 398"/><path d="M554 402 C540 392 528 392 522 398"/>
  </g>

  <!-- brows, eyes, cheeks -->
  <g filter="url(#soft)">{both(brow)}</g>
  <g filter="url(#glow)">{both(eye)}</g>
  <g filter="url(#soft)">{both(cheek)}</g>

  <!-- nose -->
  <g fill="#ff1744" filter="url(#soft)">
    <path d="M482 652 C492 650 502 654 508 664 C498 676 488 672 482 652 Z"/>
    <path d="M542 652 C532 650 522 654 516 664 C526 676 536 672 542 652 Z"/>
  </g>
  <path d="M512 520 L512 640" stroke="#ff1744" stroke-width="2" opacity="0.35"/>

  <!-- mouth -->
  <path d="M340 706 C420 752 604 752 684 706 C664 780 600 830 512 836 C424 830 360 780 340 706 Z" fill="url(#mouthG)" stroke="#ff1744" stroke-width="7" stroke-linejoin="round" filter="url(#soft)"/>
  <path d="M470 812 Q 512 792 554 812 Q 512 830 470 812 Z" fill="#ff1744" opacity="0.85"/>
  <g filter="url(#soft)">{both(fangs)}</g>
  <g>{both(drip)}</g>
  <path d="M500 742 L524 742 L512 776 Z" fill="url(#toothG)"/>
  <g filter="url(#soft)">{both(tusk)}</g>
</svg>
'''
svg = svg.replace('#05010 2','#050102')
open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'oni-pretty.svg'),'w').write(svg)
