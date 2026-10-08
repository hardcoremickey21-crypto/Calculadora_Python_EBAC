#!/bin/bash

echo "Vamos primeiro instalar nosso python3!"

sudo apt update
sudo apt install python3

echo "Tudo pronto! Agora vamos calcular!"

python3 calc_legal.py
