#!/usr/bin/env python
print "content-type: text/html"
print 
contents ='''
<html>
<head>
</head>
<body>
<!--getting started-->

<script src="//cdnjs.cloudflare.com/ajax/libs/d3/3.5.3/d3.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/topojson/1.6.9/topojson.min.js"></script>
<script src="/datamaps.usa.min.js"></script>
<div id="container" style="position: relative; width: 500px; height: 300px;"></div>

<!--usmaps only-->
<script>
    var map = new Datamap({
        element: document.getElementById('container'),
        scope: 'usa'
    });
</script>
'''
print contents
print "</body></html>"

