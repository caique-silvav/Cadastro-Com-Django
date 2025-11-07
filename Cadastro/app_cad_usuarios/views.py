# app_cad_usuarios/views.py
from django.shortcuts import render, redirect
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        idade_str = request.POST.get('idade', '').strip()

        print(f"[DEBUG] Recebido -> Nome: '{nome}', Idade: '{idade_str}'")

        # Validação rigorosa
        if nome and idade_str:
            try:
                idade = int(idade_str)
                if idade < 1 or idade > 120:
                    raise ValueError("Idade fora do intervalo válido")
                
                # Salva somente se tudo estiver certo
                Usuario.objects.create(nome=nome, idade=idade)
                print("✅ Usuário salvo com sucesso!")
            except (ValueError, TypeError) as e:
                print(f"❌ Erro ao salvar: {e}")
        else:
            print("❌ Nome ou idade vazios!")

        return redirect('listagem_usuarios')

    # Exibe lista de usuários
    contexto = {'usuarios': Usuario.objects.all()}
    return render(request, 'usuarios/usuarios.html', contexto)

def listagem_usuarios(request):
    return render(request, 'home.html')