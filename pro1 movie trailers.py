import mediafiles
import fresh_tomatoes
robo2=mediafiles.Movies("robo2.0","Scientists help the Government",
                          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjA9VGUYkCo495B"
                          "Ld8gA5pdIJ-qpPO0mgdncNhk2tY_2QUdJJx","https://www.youtube.com/watch?v=QDKY8CRe1-0")
happynewyear=mediafiles.Movies("Happy New Year","Bunch of losers to winners",
                               "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQjDQ1ln8uMZ-P66bL39F"
                               "Z2cy9ZbJLMwnY2rakkOMXJz9cnulu4A","https://www.youtube.com/watch?v=u0mrzMQJMQ8")
taxiwala=mediafiles.Movies("Taxiwala","Silent Triller",
                           "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-HEshhi"
                           "y-ZSgAJvsi4B0NDB_vlJl8sWlzwqn1sqq3rnus0-H-",
                           "https://www.youtube.com/watch?v=Lnur3SoqA3I&vl=en")
mahanati=mediafiles.Movies("Mahanati","Biopic",
                           "https://www.apherald.com/ImageStore/images/movies/"
                           "movies-wallpapers/Mahanati-Movie-New-Posters--Photos10.jpg",
                           "https://youtu.be/PLmBpf7UHJs")
toliprema=mediafiles.Movies("Toli prema","Love Entertainer","https://encrypted-tbn0.gstatic.com/images?"
                            "q=tbn:ANd9GcQ05cikyNCudFhfpjlbqHCKyNleqNfD4zHtw5B2ovAw2TnVmtXF",
                            "https://www.youtube.com/watch?v=-kFvrsAgp3M")
julai=mediafiles.Movies("Julai","Helps the police",
                        "http://content.tupaki.com/twdata/2012/0812/reviews/1344505470-nimg-Julayi-Image.jpg",
                        "https://www.youtube.com/watch?v=oNoewJIbyfA")
                          
                               
movies=[robo2,happynewyear,taxiwala,mahanati,toliprema,julai]
fresh_tomatoes.open_movies_page(movies)
              
             
