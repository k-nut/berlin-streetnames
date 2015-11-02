# streetnames-berlin

Shows if a street is named after a man or a woman. A blue line means it is named after a man, a red line after a woman.
If the line is grey no information could be found.

This is based on the little explanation texts right below the street signs.
Unfortunately this data is in openstreetmap only for a very small part of Berlin.

A python script extracts the name from the text and searches wikidata for an entity with this name. 
If it finds one it checks the gender and adds the information to the geojson.

It is still *very* beta (and unfortunately only found men until now...)
