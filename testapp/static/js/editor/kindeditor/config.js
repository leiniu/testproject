//config.js
KindEditor.ready(function (K) {
editor = K.create('textarea[name="content"]', {
    width:'800px',
    height:'400px',
filterMode: true,//是否开启过滤模式
htmlTags : {
font : ['id', 'class', 'color', 'size', 'face', '.background-color'],
div : [
'id', 'class', 'align', '.border', '.margin', '.padding', '.text-align', '.color',
'.background-color', '.font-size', '.font-family', '.font-weight', '.background',
'.font-style', '.text-decoration', '.vertical-align', '.margin-left'
],
a : ['id', 'class', 'href', 'target', 'name'],
embed : ['id', 'class', 'src', 'width', 'height', 'type', 'loop', 'autostart', 'quality', '.width', '.height', 'align', 'allowscriptaccess'],
img : ['id', 'class', 'src', 'width', 'height', 'border', 'alt', 'title', 'align', '.width', '.height', '.border'],
'ol,ul,li,blockquote,h1,h2,h3,h4,h5,h6' : [
'id', 'class', 'align', '.text-align', '.color', '.background-color', '.font-size', '.font-family', '.background',
'.font-weight', '.font-style', '.text-decoration', '.vertical-align', '.text-indent', '.margin-left'
],
pre : ['id', 'class'],
hr : ['id', 'class', '.page-break-after'],
'br,tbody,tr,strong,b,sub,sup,em,i,u,strike,s,del' : ['id', 'class'],
iframe : ['id', 'class', 'src', 'frameborder', 'width', 'height', '.width', '.height']
}
});
});
