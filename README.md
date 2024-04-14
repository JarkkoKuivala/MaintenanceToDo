# MaintenanceToDo
## Kuvaus
Projektin ideana on toteuttaa huolto-todo applikaatio. Applikaatiossa käyttäjän täytyy ensin rekisteröityä. Rekisteröitynyt käyttäjä voi, sisään kirjauduttuaan lisätä laitteita ja huoltoja. Huollot voivat olla sidottu johonkin laitteeseen. Huollot voivat olla yksittäisiä tai tietyn ajan välein toistuvia. Kun käyttäjä kuittaa huollon tehdyksi, se siirtyy tehdyt huolot välilehdelle ja jos huolto oli merkitty toistuvaksi niin uusi samanniminen huolto ilmestyy huollot sivulle, ennalta määritetyn ajan päähän. Jos käyttäjä poistaa jonkin laitteen, kaikki siihen sidotut huollot poistuvat samalla.

## Arkkitehtuuri
 - Frontend JS, React
 - Backend Python, Flask
 - Tietokanta Sqlite

## Frontend
Komponentit:
 - Navbar
 - MaintenanceList
 - MachineForm
 - MaintenanceForm
 - DoneList
 - MaintenanceRow
 - DoneRow

## Backend
	api/users [GET, POST, PUT, DELETE]
	api/devices [GET, POST, PUT, DELETE]
	api/todos [GET, POST, PUT, DELETE]
!({{github.com}}/JarkkoKuivala/MaintenanceToDo/Document/Database.png)
