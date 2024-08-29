# dodaj
Tworzenie lokalnej bazy książek, w oparciu o webscarping strony lubimyczytac.

Wymaga zewnętrznych bibliotek - bs4 i flask

Program "dodaj", dodaje książke z linka do bazy danych.
sqlread.py odczytuje tę bazę i wyświetla książki w przeglądarce pod adresem:
IP-komputera:5050/książki

Sposób użycia:

Dodanie strony do bazy danych: dodaj link-do-strony-na-lubimyczytac</br>
Usunięcie strony z bazy danych: dodaj -d link-do-strony-na-lubimyczytac</br>
Dodanie książki z własnym komentarzem lub zmiana/dodanie komentarza do istniejącej już w bazie książki: dodaj -n link-do-strony-na-lubimyczytac</br>





API
IP-komputera:5050/api
Możliwość wyszukiwania wg parametru "author" i "rate", czyli wg oceny książki podanej na stronie.

Testowane na Linuxie, rhel 8
