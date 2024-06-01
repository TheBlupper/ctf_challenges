# Mats Matrisson

Flaggan är uppdelad i tre delar och placerad på diagonelen i en diagonal matris $D$. Sedan generaras en slumpmässig inverterbar matris som vi kallar $P$ och sedan beräknas $A=PDP^{-1}$. Sedan printas spåret (trace) av $A$, $A$ stoppas in i ett polynom och förändras, determinanten printas, ett till polynom transformerar den, och till sist printas den andra koefficienten i det karaktäristiska polynomet av den nya matrisen (med "andra" menas koefficienten framför $x$).

## Egenvärden
Den tänkta lösningen bygger på egenvärderna av $A$. Egenvärden kan ibland verka lite märkliga och omotiverade, 3Blue1Brown har [en bra video](https://youtu.be/PFDu9oVAE-g) som förklarar vad egenvärden är och vad de innebär (hans serie om linjär algebra rekomenderar jag starkt).

Den geometriska intuitionen bakom egenvärden har inte så mycket betydelse I den här utmaningen, vi kommer istället använda algebraiska egenskaper hos egenvärderna och hur de påverkas av matrisoperationer. Följande fakta kommer att användas, allt finns att läsa på mer om på Wikipedia eller dylikt.

- Spåret av en matris är summan av dess egenvärden
- Determinanten av en matris är produkten av dess egenvärden
- Egenvärderna är rötterna till det karaktäristiska polynomet av en matris
- Om $\lambda$ är ett egenvärde till $A$ och $p(x)$ är ett polynom så är $p(\lambda)$ ett egenvärde till $p(A)$, egenvärdern "transformeras" alltså på samma sätt som matrisen gör

## Lösning

Det först vi bör notera är att $A=PDP^{-1}$ har samma egenvärden som $D$ eftersom $A$ och $D$ per definition är likformiga, se [här](http://www.math.chalmers.se/Math/Grundutb/CTH/tma841/1415/algebra.pdf) och sök efter `likformig`. Egenvärderna till $D$ är helt enkelt elementen på diagonalen. Egenvärderna till $A$ innan några transformationer har gjorts är alltså den uppdelade flaggan.
Låt
$$
f(x) = 8x^2 - 5x + 16 \\
g(x) = 6x^2 + 20x - 3
$$
samt låt $\lambda_1, \lambda_2$ och $\lambda_3$ vara egenvärdena till $A$ och $p_M(x)$ det karaktäristiska polynomet till en godtycklig matris $M$. Det vi har givet är $t$, $d$ och $c$ så att

$$
\begin{align}
t = & \operatorname{tr}(A) = \lambda_1 + \lambda_2 + \lambda_3 \\
d = &\operatorname{det}(f(A)) = f(\lambda_1)f(\lambda_2)f(\lambda_3) \\
c = &\text{koefficienten framför } x \text{ i } p_{g(f(A))}(x)
\end{align}
$$

$(1)$ och $(2)$ är lätta att ställa upp som symboliska uttryck och kan göras manuellt eller med valfritt CAS (computer algebra system). Försöker man lösa det kommer man dock finna att det inte finns tillräckligt med information (detta rekomenderas inte att göra för hand), vi behöver alltså även den sista ekvationen.

$(3)$ kräver att man använder [Vietas formler](https://en.wikipedia.org/wiki/Vieta%27s_formulas) som ger samband mellan koefficienterna i ett polynom och dess rötter. Det karaktäristiska polynomet $p_A(x)$ är det av en $3\times 3$ matris och kommer därför vara ett tredjegradspolynom. För enkelhetens skull säger vi att $h(x) = g(f(x))$. Om vi antar att $p_{h(A)}(x) = ax^3+bx^2+cx+d$ (vi är alltså givna $c$). Enligt [detta exempel](https://en.wikipedia.org/wiki/Vieta%27s_formulas#Example) innebär det att $\frac{c}{a} = h(\lambda_1)h(\lambda_2) + h(\lambda_1)h(\lambda_3) + h(\lambda_2)h(\lambda_3)$. Det karaktäristiska polynomet är garanterat att vara moniskt, d.v.s $a=1$. Vi har därmed vår sista ekvation $c = h(\lambda_1)h(\lambda_2) + h(\lambda_1)h(\lambda_3) + h(\lambda_2)h(\lambda_3)$. Detta system går att lösa för $\lambda_1, \lambda_2$ och $\lambda_3$ (återigen bör någon form av CAS användas) och det ger oss de tre delarna av flaggan! Ordningen är okänd, men givet att flaggan börjar på `SSM{` och slutar på `}` finns det bara en möjlig kombination.

För lösningsskript se [här](./solve.sage)