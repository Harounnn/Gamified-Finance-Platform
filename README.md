# INNOvLINK - A Gamified Finance Platform

## Introduction
This repository contains the technical phase of our platform **InnovLink** dedicated to facilitating investor discovery for startups and assisting clients in achieving their investment goals. 

## Application of the Game Theory 
{Players} = {Individual Client, StartUp Client}
{Possiblities} = {Buy,Sell,Hold}
{Payoffs} = {f(x) / x in {Possibilities}}

The model is identified as a **Repeated Game** .

The payoff is not only used based on his own strategy , but on the others too .
That is basically how game theory acts as a baseline of the platform .
It is a solid baseline that enables us to perform future updates .

## Gamification
### Concept overview
we have two actors in the platform (individuals and startups) ; each is hoping to achieve a certain goal .
This is where gamification plays its role .
### Policy
***Individuals*** : Each successful transaction rewards bonus points and each bad move will penalize him .
**How a move can be considered good or bad ?** 
eg. Player X buy a stock of a startup A in yyyy-mm-dd :
1. If the next day the stock price is higher or equals the current price it's a win win (Player X and Startup A)
2. If not than that's a lose lose .

And each day this process is repeated .

## How exactly the Platform works
### Idea overview
