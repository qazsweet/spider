# spider with Kendo
This file requests data from tables in website http://tcmspw.com/tcmspsearch.php?qr=licorice&qsr=herb_en_name&token=9282669d641bcfa010b2c5447daf5a68.

The interesting thing is that this website is build with kendo. Although it looks like a table, it is actually inserted though sql. When the contain is read, the table data could not be found in table part or tr tag, but script part with json in one line each.

Another trick caused by kendo is that the page numbers, which are actually created by Kendo. So there is no extra newtork request to change the page. This make this work easier.
