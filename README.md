# Xiputer 
A toolkit for constructing graphs and determining their chromatic number. This toolkit is not developed for 
plug and play use, but instead you will have to look into how it works and make it work for your usecase.
However i think it's a solid foundation to start from, instead of trying to start doing everything from scratch.

## How it works (if you want to use it)
- Either use one of the provided functions in generator.py to create the graph you like, or write your own code 
  to create an adjacency list of your graph.
- Then let all chromatic numbers be tested, until the graph is colorable, or try guessing the chromatic number and 
  just use this to verify it.
  
## How it works (internally)
- first the graph representation together with the guess of the chromatic number is converted into a SAT formula
  and written into a file 
- Each node gets one variable per available color, then a clause is added that ensures 
  that at least one color is assigned. Additionally we need "k choose 2" clauses to ensure that this node is not 
  assigned more than one color.
- Each edge {u,v} (u,v are nodes) gets k clause, one for every color, ensuring that u and v cannot both have that color.
- then a SAT-solver is called to determine if the formula is satisfiable. The formulas are generated in such a way,
that the graph is k-colorable if and only if the formula is satisfiable. This is also why we cannot simply 
  compute the chromatic number, but have to "guess our way up" alternatively we can also "guess our way down", this 
  might be usefull, since it seems like satisfiable instances are easier for the solver to solve (at least kissat 
  terminates quicker in these cases)

### Underlying Solver
This tool was tested and developed using [Kissat](https://github.com/arminbiere/kissat) and expects this solver
to be on path. However you can also change the constants in xiputer.py to use any solver you like. The cnf formulas 
are written in the DIMACS CNF format, which should work for most solvers. Note that if you want to change the underlying
solver you will almost definitely have to adapt the (very crude) output parsing.
Kissat was chosen, since it won the 2022 SAT competition sequential track (using a parallel solver with the right
hardware might speed things up quite a bit and if you have the resources feel free to try a cloud based solver aswell).

Furthermore this was designed to run on macos, but will most likely also work on any sort of linux machine.

### Complexity
Obviously, since determining whether a graph is k-colorable is NP-hard, for large instances this tool will not 
produce answers quickly, if at all. However it is nice to test theories in small examples. One Note is that the number
of variables of the cnf formula will be exactly the number of nodes of the graph times the number of available colors.
Moreover for each node there will be a clause with k variables and a:="k choose 2" clauses with 2 variables.
For every edge there will be k clauses with 2 variables. So in total there will be n*(k + a) + m * k clauses 

Note: Xi is the commonly used symbol for the chromatic number and then merged with computer, since this project 
aims at actually determining the chromatic number