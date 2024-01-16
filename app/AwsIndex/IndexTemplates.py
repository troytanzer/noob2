from string import Template

HTML_HEADER = Template('''<!DOCTYPE html>
<html>

<head>
    <title>Nai 7s Boys 16u Day 1 - Troy's Pics : Random (mostly rugby) Pictures</title>
    <meta charset="utf-8">
    <meta name="viewport" content="initial-scale=1.0, width=device-width">
    <link rel="stylesheet" href="../../../static/lightgallery.js/css/lightgallery.min.css">
    <link rel="stylesheet" href="../../../static/css/style.css">
</head>

<body>
    <header>
        <nav></nav>
    </header>
    <div class="gallery-wrapper">
        <h1 class="gallery-title">Nai 7s Boys 16u Day 1 - Troy's Pics</h1>
        <div class="gallery-description">Random (mostly rugby) Pictures</div>
        <div class="breadcrumbs"><a class="breadcrumb" href="/">Home</a><span class="breadcrumb">&raquo;</span><a
                class="breadcrumb" href="/gallery/NAI_7s_2023/">Nai 7s 2023</a><span class="breadcrumb">&raquo;</span><a
                class="breadcrumb" href="/gallery/NAI_7s_2023/NAI_7s_Boys_16U_Day_1/">Nai 7s Boys 16u Day 1</a></div>
        <div class="gallery" id="lightgallery">
            <div class="lds-roller" id="loading">
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
            </div>
            <div class="grid-sizer"></div>
            <div class="gutter-sizer"></div>
''')

HTML_FOOTER = Template('''
        </div>
    </div>
    <script src="../../../static/masonry-layout/masonry.pkgd.min.js"></script>
    <script src="../../../static/imagesloaded/imagesloaded.pkgd.min.js"></script>
    <script src="../../../static/lightgallery.js/js/lightgallery.min.js"></script>
    <script src="../../../static/lg-thumbnail.js/lg-thumbnail.min.js"></script>
    <script src="../../../static/lg-autoplay.js/lg-autoplay.min.js"></script>
    <script src="../../../static/lg-fullscreen.js/lg-fullscreen.min.js"></script>
    <script src="../../../static/lg-pager.js/lg-pager.min.js"></script>
    <script src="../../../static/lg-zoom.js/lg-zoom.min.js"></script>
    <script src="../../../static/lg-hash.js/lg-hash.min.js"></script>
    <script src="../../../static/lg-share.js/lg-share.min.js"></script>
    <script src="../../../static/js/main.js"></script>
    <footer> <span>&copy; 2019-2023 <a href="https://photos.troytanzer.net">Take what you
                want</a></span><span>&nbsp;|&nbsp;</span><span>Powered by <a
                href="https://github.com/brendannee/noobgallery">noobgallery</a></span></footer>
</body>

</html>''')

HTML_IMAGE = Template('''<div class="grid-item grid-item-image " data-responsive="thumbs/${file_name} 200, medium/${file_name} 600, large/${file_name} 3000" data-src="${file_name}" 
data-sub-html="&lt;p&gt;Taken Jul 21, 2023&lt;/p&gt;">
<a class="photo-link" href="${file_name}" title="${album_name} - ${file_name}"><img src="medium/${file_name}" data-aspect-ratio="1.1924592009003938" alt="${album_name} - ${file_name}"></a></div>'
''')

HTML_GALLERY = Template('''
''')
