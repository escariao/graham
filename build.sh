#!/usr/bin/env bash

echo "[BUILD] Atualizando pacotes..."
apt-get update

echo "[BUILD] Instalando Chromium e ChromeDriver..."
apt-get install -y chromium chromium-driver

echo "[BUILD] Concluído com sucesso."
