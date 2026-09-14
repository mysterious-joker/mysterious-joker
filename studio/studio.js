import * as THREE from './vendor/three.module.js';

const host = document.querySelector('#scene');
const rotateButton = document.querySelector('#rotate');
const resetButton = document.querySelector('#reset');
const selectors = [...document.querySelectorAll('[data-project]')];
const projects = [
  { name: 'SHOPPING COPILOT', short: 'Shopping Copilot', subtitle: 'CONVERSATIONAL SEARCH', color: '#719eff', url: 'https://github.com/mysterious-joker/TTSC', description: 'Shopping Copilot — an offline conversational product-search agent, built for TikTok TechJam 2026.', lines: ['Find the right thing.', '50,000 products. One conversation.', '', '> lightweight shoes for a long walk', '  Which feature matters most?', '', 'HYBRID RETRIEVAL', 'BM25 + dense embeddings', 'Python / SQLite / ONNX'] },
  { name: 'PLUTUS', short: 'Plutus', subtitle: 'FINANCIAL DASHBOARD', color: '#d6bb84', url: 'https://github.com/lzc-nus/Plutus', description: 'Plutus — a financial dashboard with portfolio and transaction workflows. Source on the NUS account.', lines: ['A clearer view of finances.', 'Portfolio. Transactions. Overview.', '', 'FRONTEND        BACKEND', 'Next.js         FastAPI', 'TypeScript      PostgreSQL', '', 'TYPED API CONTRACTS', 'A project by Two Sicilies'] },
  { name: 'GREEN CHONK', short: 'Green Chonk', subtitle: 'JAVA TASK COMPANION', color: '#99d7ad', url: 'https://github.com/lzc-nus/ip', description: 'Green Chonk — a JavaFX task companion with persistent tasks and date-aware scheduling. NUS coursework.', lines: ['A small companion. A clearer day.', 'Tasks that stay with you.', '', '> todo explore something new', '  Chomped this task!', '', 'TODOS / DEADLINES / EVENTS', 'JavaFX + a CLI fallback', 'Java / Gradle / JUnit'] }
];
let active = 0;
let updateScreen = () => {};
function selectProject(index) {
  active = index;
  selectors.forEach((button, i) => { button.classList.toggle('selected', i === index); button.setAttribute('aria-pressed', String(i === index)); });
  document.querySelector('#active-source').href = projects[index].url;
  document.querySelector('#project-description').textContent = projects[index].description;
  updateScreen(index);
}
selectors.forEach(button => button.addEventListener('click', () => selectProject(Number(button.dataset.project))));

try {
  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, preserveDrawingBuffer: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.45;
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  host.appendChild(renderer.domElement);
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(36, 1, .1, 80);
  const target = new THREE.Vector3(0, 1, 0);
  const desk = new THREE.Group();
  scene.add(desk);
  const mat = (color, roughness = .6, metalness = .05) => new THREE.MeshStandardMaterial({ color, roughness, metalness });
  const materials = { table: mat('#354052', .5, .25), edge: mat('#181e29', .45, .35), aluminum: mat('#adbbc9', .3, .5), dark: mat('#101923'), key: mat('#667585'), accent: mat('#5d8cf1', .35, .25), paper: mat('#e2e6e1'), green: mat('#709a7e'), gold: mat('#a98753', .5, .3) };
  function bevelBox(w, h, d, r, material) {
    const shape = new THREE.Shape(); const x=-w/2, y=-h/2;
    shape.moveTo(x+r,y); shape.lineTo(x+w-r,y); shape.quadraticCurveTo(x+w,y,x+w,y+r); shape.lineTo(x+w,y+h-r); shape.quadraticCurveTo(x+w,y+h,x+w-r,y+h); shape.lineTo(x+r,y+h); shape.quadraticCurveTo(x,y+h,x,y+h-r); shape.lineTo(x,y+r); shape.quadraticCurveTo(x,y,x+r,y);
    const geometry = new THREE.ExtrudeGeometry(shape,{depth:Math.max(.001,d-.04),bevelEnabled:true,bevelThickness:.02,bevelSize:.02,bevelSegments:2,steps:1,curveSegments:8});
    geometry.translate(0,0,-d/2+.02);
    const mesh = new THREE.Mesh(geometry,material); mesh.castShadow=true; mesh.receiveShadow=true; return mesh;
  }
  function add(mesh, x, y, z, parent = desk) { mesh.position.set(x,y,z); parent.add(mesh); return mesh; }
  function cylinder(r1,r2,h,material,x,y,z,parent=desk){const mesh = new THREE.Mesh(new THREE.CylinderGeometry(r1,r2,h,48),material);mesh.castShadow=true;mesh.receiveShadow=true;return add(mesh,x,y,z,parent);}
  function rod(a,b,r,material,parent=desk){const start=new THREE.Vector3(...a),end=new THREE.Vector3(...b);const mesh=new THREE.Mesh(new THREE.CylinderGeometry(r,r,start.distanceTo(end),16),material);mesh.position.copy(start).add(end).multiplyScalar(.5);mesh.quaternion.setFromUnitVectors(new THREE.Vector3(0,1,0),end.clone().sub(start).normalize());mesh.castShadow=true;parent.add(mesh);return mesh;}
  const base = add(bevelBox(6.5,3.7,.22,.24,materials.table),0,.02,0); base.rotation.x=-Math.PI/2;
  const underside=add(bevelBox(6.3,3.5,.12,.2,materials.edge),0,-.14,0);underside.rotation.x=-Math.PI/2;
  for(const x of [-2.6,2.6])for(const z of [-1.2,1.2])cylinder(.1,.12,.35,materials.dark,x,-.35,z);
  const deskmat=add(bevelBox(3.65,1.6,.045,.12,mat('#172536',.95)),.1,.155,.8);deskmat.rotation.x=-Math.PI/2;
  const monitor=new THREE.Group();add(monitor,-.25,.18,-.7);monitor.rotation.y=.04;
  const foot=add(bevelBox(1.2,.75,.08,.09,materials.aluminum),0,.07,.1,monitor);foot.rotation.x=-Math.PI/2;
  add(bevelBox(.2,.65,.16,.05,materials.aluminum),0,.42,-.05,monitor);
  add(bevelBox(3.4,2.14,.16,.1,materials.edge),0,1.68,-.02,monitor);
  add(bevelBox(3.32,2.06,.055,.075,materials.aluminum),0,1.68,.03,monitor);
  add(bevelBox(3.22,1.96,.075,.06,materials.dark),0,1.7,.073,monitor);
  const screenCanvas=document.createElement('canvas');screenCanvas.width=1280;screenCanvas.height=736;
  const context=screenCanvas.getContext('2d');const screenTexture=new THREE.CanvasTexture(screenCanvas);screenTexture.colorSpace=THREE.SRGBColorSpace;
  const screen=new THREE.Mesh(new THREE.PlaneGeometry(3.08,1.77),new THREE.MeshBasicMaterial({map:screenTexture,toneMapped:false}));add(screen,0,1.73,.12,monitor);
  screen.userData.projectMonitor=true;
  cylinder(.025,.025,.015,materials.dark,0,2.672,.075,monitor).rotation.x=Math.PI/2;
  const indicator=new THREE.Mesh(new THREE.SphereGeometry(.018,12,8),new THREE.MeshBasicMaterial({color:'#93b8ff'}));add(indicator,1.45,.73,.12,monitor);
  updateScreen=index=>{
    const p=projects[index];context.fillStyle='#101b2b';context.fillRect(0,0,1280,736);
    context.fillStyle='#203148';context.fillRect(0,0,1280,72);
    ['#d8837e','#d8be82','#83b596'].forEach((c,i)=>{context.fillStyle=c;context.beginPath();context.arc(35+i*28,36,7,0,Math.PI*2);context.fill();});
    context.fillStyle='#acbdd3';context.font='20px monospace';context.fillText('mysterious-joker / studio',155,43);
    context.fillStyle=p.color;context.font='bold 44px sans-serif';context.fillText(p.name,56,156);
    context.font='17px monospace';context.fillText(p.subtitle,58,193);
    context.fillStyle='#9db1cb';context.fillRect(56,221,1168,1);
    p.lines.forEach((line,i)=>{context.fillStyle=i===0?'#edf2f9':line.startsWith('>')?p.color:'#a8bad0';context.font=i===0?'32px sans-serif':'24px monospace';context.fillText(line,58,276+i*44);});
    context.fillStyle=p.color;context.fillRect(58,695,24,4);context.fillStyle='#8193ac';context.font='16px monospace';context.fillText(index===0?'PERSONAL / TEAM PROJECT':'NUS / lzc-nus',101,703);screenTexture.needsUpdate=true;
  }; updateScreen(0);
  const keyboard=new THREE.Group();add(keyboard,-.35,.22,.74);keyboard.rotation.y=.04;
  const keyboardBase=add(bevelBox(2.12,.82,.1,.09,materials.aluminum),0,0,0,keyboard);keyboardBase.rotation.x=-Math.PI/2;
  const keyGeometry = new THREE.BoxGeometry(.125,.055,.13);
  const keys=new THREE.InstancedMesh(keyGeometry,materials.key,52);keys.castShadow=true;keys.receiveShadow=true;const dummy=new THREE.Object3D();let keyIndex=0;
  for(let row=0;row<4;row++)for(let col=0;col<13;col++){dummy.position.set(-.91+col*.148,.08,-.285+row*.176);dummy.updateMatrix();keys.setMatrixAt(keyIndex++,dummy.matrix);} keyboard.add(keys);
  const spacebar=add(bevelBox(.7,.12,.07,.025,materials.accent),-.1,.089,.39,keyboard);spacebar.rotation.x=-Math.PI/2;
  const mouse=add(new THREE.Mesh(new THREE.SphereGeometry(1,32,24),materials.aluminum),1.16,.25,.75);mouse.scale.set(.19,.12,.28);
  add(bevelBox(.025,.025,.1,.01,materials.dark),1.16,.365,.7);
  const cable=new THREE.CatmullRomCurve3([new THREE.Vector3(.85,.16,-.5),new THREE.Vector3(1.6,.16,-.7),new THREE.Vector3(1.9,.16,-.2),new THREE.Vector3(1.8,.16,.8)]);add(new THREE.Mesh(new THREE.TubeGeometry(cable,40,.02,8,false),materials.dark),0,0,0);
  const lamp=new THREE.Group();add(lamp,-2.46,.16,-.83);
  cylinder(.35,.38,.08,materials.edge,0,0,0,lamp);
  rod([0,.04,0],[0,1.08,0],.045,materials.aluminum,lamp);rod([0,1.08,0],[.38,1.8,-.05],.04,materials.aluminum,lamp);
  for(const [x,y] of [[0,1.08],[.38,1.8]])cylinder(.095,.095,.13,materials.accent,x,y,0,lamp).rotation.x=Math.PI/2;
  const shade=cylinder(.14,.3,.3,materials.accent,.46,1.67,.04,lamp);shade.rotation.z=-.3;
  const bulb=new THREE.Mesh(new THREE.CircleGeometry(.25,40),new THREE.MeshBasicMaterial({color:'#e9eeff'}));add(bulb,.5,1.51,.04,lamp);bulb.rotation.x=-Math.PI/2;bulb.rotation.y=.3;
  const practical=new THREE.PointLight('#abcaff',1.8,3);add(practical,.5,1.43,.04,lamp);
  const mug=new THREE.Group();add(mug,2.3,.18,.8);cylinder(.23,.2,.45,materials.accent,0,.22,0,mug);
  cylinder(.195,.195,.013,mat('#49362b'),0,.451,0,mug);
  const handle=new THREE.Mesh(new THREE.TorusGeometry(.16,.045,16,32),materials.accent);add(handle,.25,.27,0,mug);
  const rim=new THREE.Mesh(new THREE.TorusGeometry(.214,.017,12,48),materials.aluminum);add(rim,0,.458,0,mug);rim.rotation.x=Math.PI/2;
  const books=[];
  for(let i=0;i<3;i++){const book=new THREE.Group();add(book,2.18,.23+i*.2,-.55);book.rotation.y=-.17+i*.12;
    const cover=add(bevelBox(.95,1.1,.15,.03,[materials.accent,materials.gold,materials.green][i]),0,0,0,book);cover.rotation.x=-Math.PI/2;
    const pages=add(bevelBox(.88,1.06,.1,.015,materials.paper),.03,0,.015,book);pages.rotation.x=-Math.PI/2;
    for(const y of [-.08,.08]){const plate=add(bevelBox(.96,1.11,.022,.015,[materials.accent,materials.gold,materials.green][i]),0,y,0,book);plate.rotation.x=-Math.PI/2;}
    book.userData.project=i;books.push(book);
  }
  const coverCanvas=document.createElement('canvas');coverCanvas.width=512;coverCanvas.height=512;const coverContext=coverCanvas.getContext('2d');coverContext.fillStyle='#63876e';coverContext.fillRect(0,0,512,512);coverContext.fillStyle='#eff3e6';coverContext.font='bold 72px sans-serif';coverContext.fillText('NUS',48,120);coverContext.font='22px monospace';coverContext.fillText('PROJECT NOTES',48,162);coverContext.fillRect(48,215,410,3);coverContext.fillText('lzc-nus',48,455);const coverTexture=new THREE.CanvasTexture(coverCanvas);coverTexture.colorSpace=THREE.SRGBColorSpace;
  const coverLabel=new THREE.Mesh(new THREE.PlaneGeometry(.85,1),new THREE.MeshBasicMaterial({map:coverTexture}));add(coverLabel,0,.095,0,books[2]);coverLabel.rotation.x=-Math.PI/2;
  const pencil=new THREE.Group();add(pencil,1.85,.2,.22);pencil.rotation.z=Math.PI/2;pencil.rotation.x=.25;cylinder(.026,.026,.9,materials.gold,0,0,0,pencil);cylinder(0,.026,.12,materials.paper,0,.51,0,pencil);
  const floor=new THREE.Mesh(new THREE.PlaneGeometry(200,200),new THREE.ShadowMaterial({opacity:.25}));floor.rotation.x=-Math.PI/2;floor.position.y=-.56;floor.receiveShadow=true;scene.add(floor);
  scene.add(new THREE.HemisphereLight('#d8e7ff','#455773',2.3));
  const key=new THREE.DirectionalLight('#eff3ff',4);key.position.set(-3,7,6);key.castShadow=true;key.shadow.mapSize.set(1024,1024);key.shadow.camera.left=-6;key.shadow.camera.right=6;key.shadow.camera.top=6;key.shadow.camera.bottom=-6;key.shadow.bias=-.001;key.shadow.normalBias=.02;scene.add(key);
  const fill=new THREE.DirectionalLight('#749cff',2.5);fill.position.set(5,3,-4);scene.add(fill);
  let azimuth=.48, elevation=.39, wantedAzimuth=.48, wantedElevation=.39;
  const reducedMotion=matchMedia('(prefers-reduced-motion: reduce)');
  let autoRotate=false, dragging=false, start=null, visible=true, moved=false, previous=0, frame;
  function resize(){const w=host.clientWidth,h=host.clientHeight;renderer.setSize(w,h);camera.aspect=w/h;camera.updateProjectionMatrix();}
  new ResizeObserver(resize).observe(host);resize();
  const pointer=new THREE.Vector2();const raycaster=new THREE.Raycaster();
  function cast(event){const rect=renderer.domElement.getBoundingClientRect();pointer.set((event.clientX-rect.left)/rect.width*2-1,-(event.clientY-rect.top)/rect.height*2+1);raycaster.setFromCamera(pointer,camera);return raycaster.intersectObjects([screen,...books],true);}
  renderer.domElement.addEventListener('pointerdown',event=>{if(event.button!==0)return;dragging=true;moved=false;start={x:event.clientX,y:event.clientY,a:wantedAzimuth,e:wantedElevation};renderer.domElement.setPointerCapture(event.pointerId);});
  renderer.domElement.addEventListener('pointermove',event=>{if(dragging&&start){const dx=event.clientX-start.x,dy=event.clientY-start.y;moved ||= Math.abs(dx)+Math.abs(dy)>7;wantedAzimuth=THREE.MathUtils.clamp(start.a-dx*.005,-.75,1.05);if(event.pointerType!=='touch')wantedElevation=THREE.MathUtils.clamp(start.e+dy*.003,.18,.75);}else{renderer.domElement.style.cursor=cast(event).length?'pointer':'grab';}});
  function end(event){if(dragging&&!moved&&event.type==='pointerup'){const hits=cast(event);if(hits.length){let object=hits[0].object;if(object===screen)selectProject((active+1)%projects.length);else{while(object.parent&&!books.includes(object))object=object.parent;const i=books.indexOf(object);if(i>=0)selectProject(i);}}}dragging=false;start=null;}
  for(const type of ['pointerup','pointercancel','lostpointercapture'])renderer.domElement.addEventListener(type,end);
  window.addEventListener('blur',()=>{dragging=false;start=null;});
  rotateButton.addEventListener('click',()=>{autoRotate=!autoRotate;rotateButton.setAttribute('aria-pressed',String(autoRotate));rotateButton.textContent=autoRotate?'Stop rotation':'Auto-rotate';});
  resetButton.addEventListener('click',()=>{wantedAzimuth=.48;wantedElevation=.39;autoRotate=false;rotateButton.setAttribute('aria-pressed','false');rotateButton.textContent='Auto-rotate';});
  function render(time){frame=requestAnimationFrame(render);if(document.hidden||!visible)return;const delta=Math.min((time-previous)/1000,.05);previous=time;
    if(autoRotate&&!dragging)wantedAzimuth=.28+Math.sin(time*.00023)*.6;
    const ease=reducedMotion.matches?1:1-Math.exp(-delta*10);azimuth+=(wantedAzimuth-azimuth)*ease;elevation+=(wantedElevation-elevation)*ease;
    const distance=host.clientWidth<500?12.7:11.5;camera.position.set(Math.sin(azimuth)*Math.cos(elevation)*distance,1+Math.sin(elevation)*distance,Math.cos(azimuth)*Math.cos(elevation)*distance);camera.lookAt(target);renderer.render(scene,camera);
  }
  new IntersectionObserver(entries=>{visible=entries[0].isIntersecting;}).observe(host);
  host.classList.add('ready');requestAnimationFrame(render);
  renderer.domElement.addEventListener('webglcontextlost',event=>{event.preventDefault();cancelAnimationFrame(frame);host.classList.remove('ready');document.querySelector('#scene-fallback').textContent='The 3D view paused. Reload to restore it, or explore the projects below.';rotateButton.disabled=true;resetButton.disabled=true;});
  if(new URLSearchParams(location.search).has('inspect'))window.studioDiagnostics=()=>({project:projects[active].short,drawCalls:renderer.info.render.calls,triangles:renderer.info.render.triangles,textures:renderer.info.memory.textures,geometries:renderer.info.memory.geometries,azimuth,elevation});
} catch(error) {
  document.querySelector('#scene-fallback').textContent='The 3D studio is unavailable in this browser. Explore every project using the links below.';
  document.querySelector('#scene-hint').textContent='Project links work without 3D.';rotateButton.disabled=true;resetButton.disabled=true;
}
