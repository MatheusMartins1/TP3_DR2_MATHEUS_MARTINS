def escreve_texto(texto,tela,cor,fonte):
    text = fonte.render(f"Matheus Martins | {texto} - TP3", 1, cor)
    tela.blit(text,  text.get_rect(centerx=tela.get_width()/2))