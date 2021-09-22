select distinct ?pers ?persLabel ?genderLabel ?org ?orgLabel ?ctryLabel
where {
    VALUES ?countries {wd:Q408 wd:Q664 wd:Q30}
    ?pers wdt:P31 wd:Q5.                  # Any instance of a human.
#    ?pers wdt:P27 wd:Q408.                # Australian
    optional {?pers wdt:P21 ?gender.}
    ?pers p:P39|p:P106 ?positions.        # Position held / occupation
    ?positions ps:P39|ps:P106 wd:Q484876. # Position is CEO
    FILTER NOT EXISTS {?positions pq:P582 ?ceo_end.}
  
    ?positions pq:P642 ?org.              # CEO of ?org
    ?org wdt:P17 ?countries.              # Org in Countries
    ?org wdt:P17 ?ctry
   
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
order by ?orgLabel
limit 200
