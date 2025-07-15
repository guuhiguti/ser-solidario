from flask import Blueprint, render_template

admin_route = Blueprint('admin', __name__)

"""
ROTAS ADMIN (CRUD - Ações + Programas + Usuários)

/Admin1309 - Tela de Login para Acessar o Painel
/Admin/dashboard - Dashboard do Admin (Visualização Geral)

Só pode acessar as rotas abaixo se estiver logado como admin:

AÇÕES
/Admin/acoes - Listagem das ações
/Admin/acoes/<acao_id> - Detalhes de uma ação específica
/Admin/acoes/<acao_id>/editar - Editar uma ação específica
/Admin/acoes/<acao_id>/deletar - Deletar uma ação específica
/Admin/acoes/novo - Criar uma nova ação


PROGRAMAS
/Admin/programas - Listagem dos programas
/Admin/programas/<programa_id> - Detalhes de um programa específico
/Admin/programas/<programa_id>/editar - Editar um programa específico
/Admin/programas/<programa_id>/deletar - Deletar um programa específico
/Admin/programas/novo - Criar um novo programa


USUÁRIOS (Famílias)

/Admin/familias - Listagem dos dados do formulario de ajuda
/Admin/familias/<familia_id> - Detalhes de uma família específica
/Admin/familias/<familia_id>/editar - Editar os dados de uma família específica
/Admin/familias/<familia_id>/deletar - Deletar uma família específica
/Admin/familias/relatorio - Gerar relatório de famílias

USUÁRIOS (Colaboradores)

/Admin/colaboradores - Listagem dos colaboradores
/Admin/colaboradores/<colaborador_id> - Detalhes de um colaborador específico
/Admin/colaboradores/<colaborador_id>/editar - Editar um colaborador específico
/Admin/colaboradores/<colaborador_id>/deletar - Deletar um colabor


"""