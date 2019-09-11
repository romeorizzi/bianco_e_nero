# Bianco e nero #

Questo problema dimostrativo è una riproposizione del problema "bianco e nero" delle OII 2002.

Trovi [versione originale](http://www.valcon.it/c/bianco-e-nero/ "versione originale del testo del problema bianco e nero nell'archivio valcon")
del testo nell'[archivio valcon](http://www.valcon.it/c/oii/ "archivio valcon, contiene molti materiali didattici" che contiene ben collocati materiali didattici relativi alla olimpiadi ed alla programmazione in generale. (Visita consigliata.)
Altrimenti, in caso di rottura dei link,
trovi il testo originale a [questo link interno](public/bianco-e-nero_testo-originale.html "copia in locale del testo originale del problema bianco e nero").

Un modo in cui la presente versione TuringArena si pone l'obiettivo di impreziosire il problema, oltre alla resa interattiva dello stesso ed al maggior feedback offerto al ragazzo in caso di sottomissioni con problemi, risiede nella formulazione e proposta di un percorso per goals che guidino il problem-solver a ricercare la comprensione prima della codifica e ad opprocciare il problema lungo un percorso di esplorazione naturale.

## Goals ##

Progetta e realizza algoritmi per:

1. Data una collana, dire quale è il minimo numero di mosse per risolverla;

2. Fornire una qualsiasi sequenza di mosse che la risolva;

3. Risolverla in al più $N^2$ mosse;

4. Fornire una sequenza risolvente ottima, ossia che contempli il minor numero possibile di mosse;

5. Fare quanto richiesto in tempo lineare nella lunghezza della collana.


## DESCRIZIONE DEL PROBLEMA ##

Vi viene data una collana costituita da&nbsp;$N$ perline bianche e nere. Ogni perlina porta impresso un numero intero da&nbsp;$1$ a&nbsp;$N$; all'inizio, leggendo i numeri delle perline in senso orario, essi compaiono consecutivamente, cioè la perlina&nbsp;$1$ è seguita dalla perlina&nbsp;$2$, che è seguita dalla perlina&nbsp;$3$ eccetera. (Naturalmente, la perlina&nbsp;$N$ è seguita dalla perlina&nbsp;$1$).

Ecco un esempio di collana di $N=9$ perline.

<center>
<IMG align="center" SRC="public/figs/oii_2002_nero1.png" width="90%" height="90%">
</center>

<!---
![Figura 1. Una collana con 9 perline.](public/figs/oii_2002_nero1.png)
-->

Il vostro obiettivo è di riordinare le perline in modo tale che alla fine le perline dello stesso colore compaiano consecutivamente, cioè tutte le perline bianche compaiano senza interruzioni, e così pure le perline nere.
Non è importante invece quale sia l'ordine numerico delle perline alla fine.

Per riordinare le perline avete a disposizione un solo tipo di operazione, detto taglia e cuci.
Questa operazione consiste nel tagliare un segmento della collana e nel reincollarlo nella stessa posizione ma rovesciato in verso.

<table align="center">
<tr align="center">
<td><IMG SRC="public/figs/oii_2002_nero1.png" width="90%" height="90%"></td>
<td><IMG SRC="public/figs/right-and-back-arrow.png" width="90%" height="90%"></td>
<td><IMG SRC="public/figs/oii_2002_nero2.png" width="90%" height="90%"></td>
</tr>
</table>

<!---
![Figura 2. La collana di Figura 1 dopo un taglia e cuci del segmento compreso fra 9 e 2.](public/figs/oii_2002_nero2.png)
-->

Con un'ulteriore operazione di taglia e cuci riusciamo ora ad ottenenere una configurazione che consideriamo risolta in quanto tutte le perle di uno stesso colore sono ora disposte consecutivamente lungo la collana.

<table align="center">
<tr align="center">
<td><IMG SRC="public/figs/oii_2002_nero2.png" width="90%" height="90%"></td>
<td><IMG SRC="public/figs/right-and-back-arrow.png" width="90%" height="90%"></td>
<td><IMG SRC="public/figs/oii_2002_nero3.png" width="90%" height="90%"></td>
</tr>
</table>


<!---
![Figura 3. La collana di Figura 2 dopo un taglia e cuci del segmento compreso fra 1 e 5.](public/figs/oii_2002_nero3.png)
-->


# INTERFACE (gestione input/output) #

Per quanto riguarda la presente versione TuringArena del roblema, si guardi il file interface.txt(public/interface.txt) e/o si parta direttamente a completare il template di soluzione per il linguaggio da voi prescelto ( C(public/template.c), C(public/template.cpp), Python(public/template.py), Rust (public/template.rs), Java (public/template.java) ). Sono tutti file che, in generale, puoi ottenere dalla pagina del problema.
In molti casi, come in questo, risultano autoesplicativi sui formati della consegna.

La versione CMS richiedeva invece di effettuare input e output via file, doveva quindi specificare i formati e proseguire precisando varie assunzioni, come ora richiamato nel proseguio di questa pagina per meglio consentire un confronto.

<h3>Dati in input</h3>
<p>Il file di input, di nome <tt>input.txt</tt>, contiene due righe.</p>
<ul>
<li>Sulla prima riga compare il singolo intero <tt>N</tt>.</li>
<li>Sulla seconda riga compaiono esattamente <tt>N</tt> caratteri, ciascuno dei quali è una <tt>B</tt> oppure una <tt>N</tt>.<br />
In particolare, l&#8217;<tt>i</tt>-esimo carattere indica il colore della perlina numero <tt>i</tt> (<tt>B</tt> sta per <em>bianco</em> mentre <tt>N</tt> sta per <em>nero</em>).</li>
</ul>
<h3>Dati in output</h3>
<p>Il file di output, di nome <tt>output.txt</tt>, contiene la sequenza di operazioni taglia e cuci da effettuare per riordinare correttamente le perline.<br />
Ciascuna riga è costituita da due numeri interi (separati da uno spazio), che sono il numero della prima e dell&#8217;ultima (in senso orario) perlina del segmento che viene tagliato e reincollato.</p>

<h3>Assunzioni</h3>
<ul>
<li>il tempo limite di esecuzione è fissato in 2 secondi;</li>
<li><tt>1 &lt;= N &lt;= 1000</tt>;</li>
<li>la collana potrebbe contenere anche perline tutte dello stesso colore (in questo caso, il file di output dovrebbe essere vuoto).</li>
</ul>
<h3>Esempio</h3>
<div class="indent">
<table class="data">
<tbody>
<tr>
<th>input.txt</th>
<th>output.txt</th>
</tr>
<tr>
<td><tt>9<br />
NBNNBNBBN</tt></td>
<td><tt>9 2<br />
1 5</tt></td>
</tr>
</tbody>
</table>
</div>
<p>L&#8217;esempio è quello mostrato in <em>Figura 1</em>.<br />
La sequenza di operazioni indicata nel file di output è quella indicata nelle <em>Figure 2</em> e <em>3</em>.</p>
