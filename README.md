# ConstructionProject

Partendo da un problema di rappresentazione di operai che lavorano in un cantiere che contiene dei tralicci sui quali gli operai eseguono i loro lavori, implementare il database e gli endpoint necessari ad ottenere delle rappresentazioni filtrabili dinamicamente dalla stesse requests.


Considerando che un traliccio può essere associato solo ad un cantiere, che un cantiere può avere più di un traliccio associato, che un operaio può essere impegnato in un solo lavoro per volta, che in un lavoro eseguito su un traliccio possono essere associati uno o più operai, che un lavoro può essere eseguito o sulla base del traliccio o sulla punta del traliccio, che un lavoro ha 4 stati: attivo, annullato, in attesa, finito e che lo storico dei lavori eseguiti viene mantenuto nel sistema, di seguito sono elencate le entità principali del problema con i relativi campi più significativi (una delle entità è omessa):


L’operaio è un utente del sistema rappresentato dai seguenti campi:

Nome

Cognome

email

tipologia utente


Il cantiere è rappresentato dai seguenti campi:

Nome


Il traliccio è rappresentato dai seguenti campi:

numero di traliccio

superficie base

superficie punta

superficie totale


Obbiettivo:

poter filtrare in maniera dinamica, attraverso delle chiamate effettuate su postman o similare, l’elenco degli operai, per determinare:

quelli che sono impegnati in un lavoro e quelli che non sono impegnati;

quelli che sono impegnati in un lavoro nella base o nella punta;

quelli che hanno eseguito un lavoro iniziato tra due date, esempio: tra il 01/12/2022 ed il 31/12/2022;

quelli che non hanno mai lavorato e quelli che hanno almeno un lavoro
