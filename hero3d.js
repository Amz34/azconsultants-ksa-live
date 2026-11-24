/* Lightweight wireframe globe for the hero band. No libraries, no faces, no photos:
   a slow rotating latitude / longitude cage drawn on a 2D canvas. Pauses when the
   hero scrolls away and renders a single static frame when motion is reduced. */
(function () {
  var canvas = document.getElementById('hero-canvas');
  if (!canvas || !canvas.getContext) { return; }
  var ctx = canvas.getContext('2d');
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var LAT = 7, LON = 12, R = 1, FOV = 3.2;
  var nodes = [];

  function build() {
    nodes = [];
    for (var i = 1; i < LAT; i++) {
      var phi = (Math.PI * i) / LAT, ring = [];
      for (var j = 0; j < LON; j++) {
        var theta = (2 * Math.PI * j) / LON;
        ring.push([Math.sin(phi) * Math.cos(theta), Math.cos(phi), Math.sin(phi) * Math.sin(theta)]);
      }
      nodes.push(ring);
    }
  }

  var t = 0;
  function project(p, spin, size, cx, cy) {
    var x = p[0] * Math.cos(spin) - p[2] * Math.sin(spin);
    var z = p[0] * Math.sin(spin) + p[2] * Math.cos(spin);
    var tilt = 0.42, y = p[1] * Math.cos(tilt) - z * Math.sin(tilt);
    var zz = p[1] * Math.sin(tilt) + z * Math.cos(tilt);
    var s = R * size / (FOV + zz);
    return [cx + x * s, cy - y * s, zz];
  }

  function fit() {
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var r = canvas.getBoundingClientRect();
    canvas.width = Math.max(1, Math.floor(r.width * dpr));
    canvas.height = Math.max(1, Math.floor(r.height * dpr));
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    return r;
  }

  var box = fit();
  function draw() {
    box = canvas.getBoundingClientRect();
    var w = box.width, h = box.height;
    ctx.clearRect(0, 0, w, h);
    var size = Math.min(w, h) * 0.46, cx = w * 0.74, cy = h * 0.5;
    ctx.lineWidth = 1;
    for (var i = 0; i < nodes.length; i++) {
      var ring = nodes[i];
      ctx.beginPath();
      for (var j = 0; j <= LON; j++) {
        var p = project(ring[j % LON], t, size, cx, cy);
        var depth = (p[2] + 1) / 2;
        if (j === 0) { ctx.moveTo(p[0], p[1]); } else { ctx.lineTo(p[0], p[1]); }
        ctx.strokeStyle = 'rgba(31, 74, 52, ' + (0.10 + depth * 0.22).toFixed(3) + ')';
      }
      ctx.stroke();
    }
    for (var k = 0; k < LON; k++) {
      ctx.beginPath();
      for (var m = 0; m <= nodes.length; m++) {
        var q = nodes[m % nodes.length][k];
        var pp = project(q, t, size, cx, cy);
        if (m === 0) { ctx.moveTo(pp[0], pp[1]); } else { ctx.lineTo(pp[0], pp[1]); }
      }
      ctx.strokeStyle = 'rgba(31, 74, 52, 0.16)';
      ctx.stroke();
    }
    ctx.beginPath();
    ctx.arc(cx, cy, size * 0.85, 0, Math.PI * 2);
    ctx.strokeStyle = 'rgba(31, 74, 52, 0.14)';
    ctx.stroke();
  }

  build();
  var running = !reduce;
  if (reduce) { draw(); }

  function loop() {
    if (!running) { return; }
    t += 0.0035;
    draw();
    requestAnimationFrame(loop);
  }
  if (!reduce) { requestAnimationFrame(loop); }

  window.addEventListener('resize', function () { fit(); if (reduce) { draw(); } });
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (entries) {
      var visible = entries[0].isIntersecting;
      if (visible && !reduce && !running) { running = true; requestAnimationFrame(loop); }
      if (!visible) { running = false; }
    }, { threshold: 0 }).observe(canvas);
  }
})();
