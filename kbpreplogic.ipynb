{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "z_9huN8cp7yf"
      },
      "outputs": [],
      "source": [
        "combinations=[(True,True, True),(True,True,False),(True,False,True),(True,False, False),(False,True, True),(False,True, False),(False, False,True),(False,False, False)]\n",
        "variable={'p':0,'q':1, 'r':2}\n",
        "kb=''\n",
        "q=''\n",
        "priority={'~':3,'v':1,'^':2}"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def input_rules():\n",
        "    global kb, q\n",
        "    kb = (input(\"Enter rule: \"))\n",
        "    q = input(\"Enter the Query: \")"
      ],
      "metadata": {
        "id": "SnU2QliWp-yM"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def entailment():\n",
        "    global kb, q\n",
        "    print('*'*10+\"Truth Table Reference\"+'*'*10)\n",
        "    print('kb','alpha')\n",
        "    print('*'*10)\n",
        "    for comb in combinations:\n",
        "        s = evaluatePostfix(toPostfix(kb), comb)\n",
        "        f = evaluatePostfix(toPostfix(q), comb)\n",
        "        print(s, f)\n",
        "        print('-'*10)\n",
        "        if s and not f:\n",
        "            return False\n",
        "    return True"
      ],
      "metadata": {
        "id": "bcAgSuBpqIas"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def isOperand(c):\n",
        "    return c.isalpha() and c!='v'\n",
        "\n",
        "def isLeftParanthesis(c):\n",
        "    return c == '('\n",
        "\n",
        "def isRightParanthesis(c):\n",
        "    return c == ')'\n",
        "\n",
        "def isEmpty(stack):\n",
        "    return len(stack) == 0\n",
        "\n",
        "def peek(stack):\n",
        "    return stack[-1]\n",
        "\n",
        "def hasLessOrEqualPriority(c1, c2):\n",
        "    try:\n",
        "        return priority[c1]<=priority[c2]\n",
        "    except KeyError:\n",
        "        return False"
      ],
      "metadata": {
        "id": "2at0l5aQqK-0"
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def toPostfix(infix):\n",
        "    stack = []\n",
        "    postfix = ''\n",
        "    for c in infix:\n",
        "        if isOperand(c):\n",
        "            postfix += c\n",
        "        else:\n",
        "            if isLeftParanthesis(c):\n",
        "                stack.append(c)\n",
        "            elif isRightParanthesis(c):\n",
        "                operator = stack.pop()\n",
        "                while not isLeftParanthesis(operator):\n",
        "                    postfix += operator\n",
        "                    operator = stack.pop()\n",
        "            else:\n",
        "                while (not isEmpty(stack)) and hasLessOrEqualPriority(c, peek(stack)):\n",
        "                    postfix += stack.pop()\n",
        "                stack.append(c)\n",
        "    while (not isEmpty(stack)):\n",
        "        postfix += stack.pop()\n",
        "    \n",
        "    return postfix"
      ],
      "metadata": {
        "id": "ymnFtzk3qNmk"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def evaluatePostfix(exp, comb):\n",
        "    stack = []\n",
        "    for i in exp:\n",
        "        if isOperand(i):\n",
        "            stack.append(comb[variable[i]])\n",
        "        elif i == '~':\n",
        "            val1 = stack.pop()\n",
        "            stack.append(not val1)\n",
        "        else:\n",
        "            val1 = stack.pop()\n",
        "            val2 = stack.pop()\n",
        "            stack.append(_eval(i,val2,val1))\n",
        "    return stack.pop()"
      ],
      "metadata": {
        "id": "r8dFJLQhqSrF"
      },
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def _eval(i, val1, val2):\n",
        "    if i == '^': \n",
        "        return val2 and val1\n",
        "    return val2 or val1"
      ],
      "metadata": {
        "id": "apnrdwZuqVuE"
      },
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "input_rules()\n",
        "ans = entailment()\n",
        "if ans:\n",
        "    print(\"The Knowledge Base entails query\")\n",
        "else:\n",
        "    print(\"The Knowledge Base does not entail query\")\n"
      ],
      "metadata": {
        "id": "dB_rhkT_qbts",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c6759ce7-80b3-44b2-9723-d3bfa240fb6e"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter rule: (~qv~pvr)^(~q^p)^q\n",
            "Enter the Query: r\n",
            "**********Truth Table Reference**********\n",
            "kb alpha\n",
            "**********\n",
            "False True\n",
            "----------\n",
            "False False\n",
            "----------\n",
            "False True\n",
            "----------\n",
            "False False\n",
            "----------\n",
            "False True\n",
            "----------\n",
            "False False\n",
            "----------\n",
            "False True\n",
            "----------\n",
            "False False\n",
            "----------\n",
            "The Knowledge Base entails query\n"
          ]
        }
      ]
    }
  ]
}
