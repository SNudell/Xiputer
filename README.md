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
- then a SAT-solver is called to determine if the formula is satisfiable. The formulas are generated in such a way,
that the graph is k-colorable if and only if the formula is satisfiable. This is also why we cannot simply
  compute the chromatic number, but have to "guess our way up"

### Underlying Solver
This tool was tested and developed using [Kissat](https://github.com/arminbiere/kissat) and expects this solver
to be on path. However you can also change the constants in xiputer.py to use any solver you like. The cnf formulas 
are written in the DIMACS CNF format, which should work for most solvers. Note that if you want to change the underlying
solver you will almost definitely have to adapt the (very crude) output parsing.

Furthermore this was designed to run on macos, but will most likely also work on any sort of linux machine.

Note: Xi is the commonly used symbol for the chromatic number and then merged with computer, since this project 
aims at actually determining the chromatic number