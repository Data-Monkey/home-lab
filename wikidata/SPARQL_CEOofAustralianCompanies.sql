select distinct ?pers ?persLabel ?genderLabel ?orgLabel 
where {
    ?pers wdt:P31 wd:Q5.  # Any instance of a human.
#    ?pers wdt:P27 wd:Q408.  # Australian
    optional {?pers wdt:P21 ?gender.}
    ?pers p:P39 ?positions.
    ?positions ps:P39 wd:Q484876. # Position is CEO
    ?positions pq:P642 ?org.
    ?org wdt:P17 wd:Q408.   # Org in Australia
               
   
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
order by ?orgLabel
limit 200

