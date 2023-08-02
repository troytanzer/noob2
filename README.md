# noob2
Fork of noob gallery to match my workflow

## Why????

I tested out [[noobgallery][https://github.com/brendannee/noobgallery]] for hosting an S3 static site of pictures and mostly liked it, but it didn't quite fit my workflow.

I was looking at hosting all of my sports pics in albums, and my first impression was that it fit the bill - no login required, simple and useful viewer, sorted by directory structure, etc.

The two main problems were :

 - It required all the photos for the site to be processed at once.  It needed to be on the disk in the correct structure, and then each build, thumbnail generation, and upload would wipe the site clean and upload fresh.  That got old for more than a few albums.

 - Once you have so many photos, it would run out of memory and freeze up my laptop doing the resizing operations.  Haven't looked into this, but old versions of imagemagick did the same thing - if you selected a wildcard pattern, all images were loaded into memory and worked on at once.

I broke the project into two parts - one is the local management of photos.  I changed it so that it points at an S3 bucket and then navigates through the photos and generates the index files (and thumbnails, if needed) and then uploads just the index files into the correct directories. I just can't grok javascript, so this piece is in python.  For my workflow, I take a ton of photos, and then sort them into various folders for posting on IG, sending to specific people, populating this web site, sending to my backup solution, etc.  So, just uploading a folder of images to S3 works better than having to create and maintain a complete local copy of the site, and speeds up the process of uploading photos after games.  Also, depending on that games/tournaments I'm shooting, I'm on a bunch of different computers that may or may not have access to my nfs that stores and backs up my photos.  Not great to have to mirror 100 GB of images all over the place just to be able to upload a couple dozen new images.

The second piece is basically untouched - it is the javascript libraries that look at the index files and provide navigation on the site and a lightbox view of the photos that looks great on a browser and on a phone.  Big black box there for me.

## Usage

We shall see.