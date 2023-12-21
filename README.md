# Olho Vigilante

## Descrição do Projeto
O projeto "Olho Vigilante" é uma aplicação Python que utiliza a biblioteca OpenCV e a interface gráfica Tkinter para detectar movimentos na webcam do computador. Ele oferece a capacidade de identificar movimentos na cena capturada pela câmera e, quando um movimento é detectado, minimiza automaticamente todas as janelas do Google Chrome. Esse projeto pode ser útil em situações em que você deseja manter o foco no seu trabalho e deseja evitar distrações no navegador da web.

## Funcionalidades
- Captura o feed de vídeo da webcam do computador.
- Aplica o algoritmo de subtração de fundo MOG2 para detectar áreas em movimento na cena.
- Identifica contornos nas áreas em movimento.
- Quando um movimento é detectado (com base em um limite de área configurável), ele destaca as áreas em movimento com retângulos verdes no vídeo.
- Minimiza automaticamente todas as janelas do Google Chrome quando o movimento é detectado.
- Oferece um botão "Fechar" para encerrar o programa.

## Requisitos
- Python 3.x instalado.
- As bibliotecas Python: OpenCV, pyautogui, tkinter e Pillow (PIL).

## Uso
1. Execute o script Python após garantir que todas as bibliotecas necessárias estão instaladas.
2. A interface gráfica será exibida com um botão "Fechar".
3. O feed de vídeo da webcam será mostrado na janela principal.
4. Quando ocorrer movimento na cena, as áreas em movimento serão destacadas com retângulos verdes.
5. Todas as janelas do Google Chrome serão minimizadas automaticamente quando ocorrer movimento na cena.
6. Para encerrar o programa, clique no botão "Fechar" ou feche a janela principal.

## Configuração
- Você pode ajustar o limite de área de detecção de movimento alterando o valor `cv2.contourArea(c) < 500`. Valores maiores detectarão apenas movimentos maiores e valores menores detectarão movimentos menores.

## Limpeza
Certifique-se de liberar a câmera e fechar todas as janelas gráficas quando o programa for encerrado. Isso é feito automaticamente no script.

## Autor
Este projeto foi desenvolvido por [Seu Nome/Apelido] e está disponível sob a licença [licença] para uso e distribuição.

## Notas
- Este projeto pode ser personalizado e aprimorado para atender às suas necessidades específicas.
- Certifique-se de ter permissão para usar a webcam e manipular janelas do Google Chrome no seu sistema operacional.
- Certifique-se de fornecer um ícone personalizado ao usar o PyInstaller para criar um executável único.

Aproveite o uso do "Olho Vigilante" e mantenha o foco em seu trabalho!
