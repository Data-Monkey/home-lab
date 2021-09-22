SELECT DISTINCT ?org ?orgLabel ?ceo ?ceoLabel ?ceo_start ?chairLabel
  
WHERE
{  
   VALUES ?industries {wd:Q650241 wd:Q22687}  #Financial Institution or Bank 
   ?org wdt:P31/wdt:P279* wd:Q43229.          # Organisation or subclass 
 #  ?org wdt:P17  wd:Q408.                     # country = Australia
   ?org wdt:P31  ?industries .                # Instance Of Industries defined above 

    OPTIONAL {
  ?org p:P169 ?ceo_position.
  ?ceo_position ps:P169 ?ceo.
  ?ceo_position pq:P580 ?ceo_start.
  FILTER NOT EXISTS {?ceo_position pq:P582 ?ceo_end.}
}
  OPTIONAL {
    ?org p:P488 ?chairperson_position.
    ?chairperson_position ps:P488 ?chair.
    FILTER NOT EXISTS {?chairperson_position pq:P582 ?chair_end.}
  }

      
   SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
ORDER BY ?ceoLabel 
limit 200

#?org wdt:P31 wd:Q891723.  #instance of public company
#?org wdt:P414 wd:Q732670. #listed at exchange ASX     

#?org wdt:P3320 ?boardMembers #has board members
#?org wdt:P3320 ?boardMembers #has board members

  #   ?org wdt:P414 wd:Q82059.  #NASDAQ
