{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fa3fc918-6ea8-4b79-8d07-cdafb24be8c3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\t\t\t\t\t\tRock Paper Scissor\n",
      "\n",
      "Rules of Game : \n",
      "\n",
      "1.Rock VS Paper ====> Paper wins\n",
      "2.Rock VS Scissor ====> Rock wins\n",
      "3.Scissor VS Paper ====> Scissor wins\n",
      "\n",
      "\n",
      "==>A win in each round gains a point.\n",
      "==>Gaining 3 points declares the WINNER.\n",
      "\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your name:\n",
      " Hari\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "let's Begin the Game\n",
      "\n",
      "1.Rock\n",
      "2.Paper\n",
      "3.Scissor\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your Choice: 1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your Choice is:rock\n",
      "Computr's choice:scissor\n",
      "rock  VS  scissor\n",
      "Hari  win's\n",
      "\n",
      "Points ==> computer=  0 \t\t Hari =  1\n",
      "1.Rock\n",
      "2.Paper\n",
      "3.Scissor\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your Choice: 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your Choice is:paper\n",
      "Computr's choice:paper\n",
      "paper  VS  paper\n",
      "It'a a tie.\n",
      "Points ==> computer=  0 \t\t Hari =  1\n",
      "1.Rock\n",
      "2.Paper\n",
      "3.Scissor\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your Choice: 1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your Choice is:rock\n",
      "Computr's choice:paper\n",
      "rock  VS  paper\n",
      "Computer win's\n",
      "\n",
      "Points ==> computer=  1 \t\t Hari =  1\n",
      "1.Rock\n",
      "2.Paper\n",
      "3.Scissor\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your Choice: 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your Choice is:scissor\n",
      "Computr's choice:paper\n",
      "scissor  VS  paper\n",
      "Hari  win's\n",
      "\n",
      "Points ==> computer=  1 \t\t Hari =  2\n",
      "1.Rock\n",
      "2.Paper\n",
      "3.Scissor\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your Choice: 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your Choice is:paper\n",
      "Computr's choice:scissor\n",
      "paper  VS  scissor\n",
      "Computer win's\n",
      "\n",
      "Points ==> computer=  2 \t\t Hari =  2\n",
      "1.Rock\n",
      "2.Paper\n",
      "3.Scissor\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your Choice: 1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your Choice is:rock\n",
      "Computr's choice:scissor\n",
      "rock  VS  scissor\n",
      "Hari  win's\n",
      "\n",
      "Points ==> computer=  2 \t\t Hari =  3\n",
      "------ Hari  Win's------\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Do you want to play again!!\n",
      "YES=Y\n",
      "NO=N N\n"
     ]
    }
   ],
   "source": [
    "import random as r\n",
    "print(\"\\t\\t\\t\\t\\t\\tRock Paper Scissor\\n\")\n",
    "print(\"Rules of Game : \\n\")\n",
    "print(\"1.Rock VS Paper ====> Paper wins\\n2.Rock VS Scissor ====> Rock wins\\n3.Scissor VS Paper ====> Scissor wins\\n\\n\")\n",
    "print(\"==>A win in each round gains a point.\\n==>Gaining 3 points declares the WINNER.\\n\\n\")\n",
    "name=input(\"Enter your name:\\n\")\n",
    "possibilities=[\"rock\",\"paper\",\"scissor\"]\n",
    "print(\"let's Begin the Game\\n\")\n",
    "ch='Y'\n",
    "cl=0\n",
    "hl=0\n",
    "while(ch=='Y'):\n",
    "    print(\"1.Rock\\n2.Paper\\n3.Scissor\\n\")\n",
    "    choice=int(input(\"Enter your Choice:\"))\n",
    "    a=possibilities[choice-1]\n",
    "    b=r.choice(possibilities)\n",
    "    print(\"Your Choice is:\"+a)\n",
    "    print(\"Computr's choice:\"+b)\n",
    "    print(a,\" VS \",b)\n",
    "    if(a==\"rock\" and b==\"scissor\"):\n",
    "        print(name,\" win's\\n\")\n",
    "        hl+=1\n",
    "        print(\"Points ==> computer= \",cl,\"\\t\\t\",name,\"= \",hl)\n",
    "    if(a==\"rock\" and b==\"paper\"):\n",
    "        print(\"Computer win's\\n\")\n",
    "        cl+=1\n",
    "        print(\"Points ==> computer= \",cl,\"\\t\\t\",name,\"= \",hl)\n",
    "    if(a==\"paper\" and b==\"scissor\"):\n",
    "        print(\"Computer win's\\n\")\n",
    "        cl+=1\n",
    "        print(\"Points ==> computer= \",cl,\"\\t\\t\",name,\"= \",hl)\n",
    "    if(a==\"paper\" and b==\"rock\"):\n",
    "        print(name,\" win's\\n\")\n",
    "        hl+=1\n",
    "        print(\"Points ==> computer= \",cl,\"\\t\\t\",name,\"= \",hl)\n",
    "    if(a==\"scissor\" and b==\"rock\"):\n",
    "        print(\"computer win's\\n\")\n",
    "        cl+=1\n",
    "        print(\"Points ==> computer= \",cl,\"\\t\\t\",name,\"= \",hl)\n",
    "    if(a==\"scissor\" and b==\"paper\"):\n",
    "        print(name,\" win's\\n\")\n",
    "        hl+=1\n",
    "        print(\"Points ==> computer= \",cl,\"\\t\\t\",name,\"= \",hl)\n",
    "    if(a==\"scissor\" and b==\"scissor\"):\n",
    "        print(\"It'a a tie.\")\n",
    "        print(\"Points ==> computer= \",cl,\"\\t\\t\",name,\"= \",hl)\n",
    "    if(a==\"rock\" and b==\"rock\"):\n",
    "        print(\"It'a a tie.\")\n",
    "        print(\"Points ==> computer= \",cl,\"\\t\\t\",name,\"= \",hl)\n",
    "    if(a==\"paper\" and b==\"paper\"):\n",
    "        print(\"It'a a tie.\")\n",
    "        print(\"Points ==> computer= \",cl,\"\\t\\t\",name,\"= \",hl)\n",
    "    if(cl==3 or hl==3):\n",
    "        if(hl==3):\n",
    "            print(\"------\",name,\" Win's------\")\n",
    "        else:\n",
    "            print(\"------Computer Win's------\")\n",
    "        ch=input(\"Do you want to play again!!\\nYES=Y\\nNO=N\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ab3afade-a9ae-43d1-85e2-f05c945e476d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
