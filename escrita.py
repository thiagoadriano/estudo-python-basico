# -*- encoding: utf-8 -*-
arquivo = open('texto_escrita.txt', 'a', encoding='utf-8')

arquivo.write("é apenas um teste de um textão\n")
arquivo.write("é apenas um teste de um textão\n")
arquivo.writelines("é apenas um teste de um textão 3\n")

arquivo.close()