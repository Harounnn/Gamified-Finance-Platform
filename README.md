# INNOvLINK - A Gamified Finance Platform

## Introduction
This repository contains the technical phase of our platform **INNOvLINK** dedicated to facilitating investment discovery for startups and assisting clients in achieving their investment goals. 

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

## How exactly the Platform works ?
### Idea overview
For an individual, it is as easy as just signing up to the platform and starting his journey .
This journey is basically creating a 'Project' (ie. Kind of folder to start trading for a certain reason where you have to enter your budget and the desired amount). Here, our job is to provide the user some information about the startups present in our platform using AI . For more details check the next section .
This recommendation is based on your level as a "Player" (eg. Player X is level 3 and Player Y is level 5, the Player Y will get the forcasting for the next n days but the Player X will just be limited to n/2 days).

For a StartUp, our platform will be a provider of well-designed and easy-to-understand dashboards, next to 
the gamification algorithm which rewards the startup by raising its chances to be recommended to end users , based on the level and/or score of the startup and of course based on its real-world performance .

### The Forecasting AI model and Future work
#### Model Architecture
As a baseline model , we chose the LSTM-based RNN . 
***Why ?***

The RNN model architecture is known by its Past Information Gathering through time , and that's exactly what we need it to do .
BUT, after some little research we found that the task of studying stock market should be treated by an auto-regressive model because of its unstable pattern . And, we have an LSTM baseline model so we will choose a DeepAR-like architecture with some fine tuning to our customized dataset.  

#### Future Work
At this moment, we did not advanced a lot in the dev stage but the idea is clarified .
Soon, the dev team will start working on each component individually : from Front-End web development to the building of the AI API which will be deployed to cloud as soon as the model is ready for going through the DEVOPS pipeline .
We are full of ideas (hopefully came true features of our application).
