import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Lista de serviços para as descrições de entrada
SERVICES = [
    "Cartões de Visita", "Panfletos e Folders", "Banners e Faixas", "Adesivos e Etiquetas", "Convites Personalizados", 
    "Calendários", "Encadernação", "Laminação", "Plastificação", "Identidade Visual", "Agendas", "Canecas",
    "Camisetas", "Bordados", "Lembrancinhas", "Sacolinhas Personalizadas", "Rótulos", "Tags", "Topos de Bolo",
    "Bottons", "Chaveiros"
]

# Inicializa o banco de dados
def init_db():
    with sqlite3.connect('cashflow_system.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL,  -- 'entrada' ou 'saida'
                category TEXT NOT NULL,  -- Tipo da transação (ex: vendas, despesas)
                description TEXT NOT NULL,  -- Descrição do produto ou serviço
                amount REAL NOT NULL  -- Valor da transação
            )
        ''')

# Limpa os campos de entrada
def clear_fields(entries):
    for entry in entries:
        entry.delete(0, tk.END)

# Tela inicial
def start_screen():
    for widget in root.winfo_children():
        widget.destroy()

    title_label = tk.Label(root, text="ATELIÊ DA RÔH", font=("Georgia", 45, 'bold'), bg='#195074', fg='white')
    title_label.pack(pady=60, expand=True, anchor='center')

   
    button_exit = tk.Button(root, text="❌", command=exit_app, width=3, height=1, font=("Arial", 14), bg='#9c0720', fg='white')
    button_exit.place(relx=1.0, rely=0.0, anchor='ne')  # Posiciona no canto superior direito

    menu_button = tk.Button(root, text="Menu 🏠", command=home_screen, width=15, height=3, font=("Arial", 14), bg='#2196F3', fg='white')
    menu_button.pack(pady=20, side=tk.BOTTOM)

# Tela do menu
def home_screen():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Sistema de Fluxo de Caixa", font=("Georgia", 24, 'bold'), bg='#195074', fg='white').pack(pady=20)

    menu_frame = tk.Frame(root, bg='#195074')  # Define a cor de fundo do frame do menu
    menu_frame.pack(pady=20)

    button_specs = [
        ("Registrar Entrada ➕", register_income_screen, '#4CAF50'),  # Verde
        ("Registrar Saída ➖", register_expense_screen, '#F44336'),  # Vermelho
        ("Fluxo de Caixa 📊", view_cashflow, '#2196F3')   # Azul
    ]

    for text, command, color in button_specs:
        button = tk.Button(menu_frame, text=text, command=command, width=30, height=3, font=("Arial", 14), bg=color, fg='white')
        button.pack(side=tk.TOP, padx=10, pady=10)

    button_back = tk.Button(root, text="⬅️", command=start_screen, width=3, height=1, font=("Arial", 14), bg='#00003d', fg='white')
    button_back.place(relx=0.0, rely=0.0, anchor='nw')  # Posiciona no canto superior esquerdo
    button_exit = tk.Button(root, text="❌", command=exit_app, width=3, height=1, font=("Arial", 14), bg='#9c0720', fg='white')
    button_exit.place(relx=1.0, rely=0.0, anchor='ne')  # Posiciona no canto superior direito

# Tela de registro de entrada (vendas de produtos/serviços)
def register_income_screen():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Registrar Entrada", font=("Georgia", 40, 'bold'), bg='#195074', fg='white').pack(pady=20)

    form_frame = tk.Frame(root, bg='#195074')
    form_frame.pack(pady=20)

    tk.Label(form_frame, text="Categoria:", bg='#195074', fg='white', font=("Arial", 16)).grid(row=0, column=0, padx=10, pady=10, sticky='e')
    category_entry = ttk.Combobox(form_frame, values=["Vendas de Produtos", "Serviços Prestados"], font=("Arial", 14), width=30)
    category_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(form_frame, text="Descrição:", bg='#195074', fg='white', font=("Arial", 16)).grid(row=1, column=0, padx=10, pady=10, sticky='e')
    description_entry = ttk.Combobox(form_frame, values=SERVICES, font=("Arial", 14), width=30)
    description_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(form_frame, text="Valor:", bg='#195074', fg='white', font=("Arial", 16)).grid(row=2, column=0, padx=10, pady=10, sticky='e')
    amount_entry = tk.Entry(form_frame, font=("Arial", 14), width=30)
    amount_entry.grid(row=2, column=1, padx=10, pady=10)
    
    tk.Button(form_frame, text="Salvar💾", command=lambda: save_transaction("entrada", category_entry, description_entry, amount_entry), font=("Arial", 14)).grid(row=3, columnspan=2, pady=20)

    button_exit = tk.Button(root, text="❌", command=exit_app, width=3, height=1, font=("Arial", 14), bg='#9c0720', fg='white')
    button_exit.place(relx=1.0, rely=0.0, anchor='ne')  # Posiciona no canto superior direito

    button_back = tk.Button(root, text="⬅️", command=home_screen, width=3, height=1, font=("Arial", 14), bg='#00003d', fg='white')
    button_back.place(relx=0.0, rely=0.0, anchor='nw')  # Posiciona no canto superior esquerdo

# Tela de registro de saída (gastos)
def register_expense_screen():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Registrar Saída", font=("Georgia", 40, 'bold'), bg='#195074', fg='white').pack(pady=20)

    form_frame = tk.Frame(root, bg='#195074')
    form_frame.pack(pady=20)

    tk.Label(form_frame, text="Categoria:", bg='#195074', fg='white', font=("Arial", 16)).grid(row=0, column=0, padx=10, pady=10, sticky='e')
    category_entry = ttk.Combobox(form_frame, values=[
        "Materiais", "Equipamentos", "Pagamentos", "Outras Despesas"
    ], font=("Arial", 14), width=30)
    category_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(form_frame, text="Descrição:", bg='#195074', fg='white', font=("Arial", 16)).grid(row=1, column=0, padx=10, pady=10, sticky='e')
    description_entry = tk.Entry(form_frame, font=("Arial", 14), width=30)
    description_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(form_frame, text="Valor:", bg='#195074', fg='white', font=("Arial", 16)).grid(row=2, column=0, padx=10, pady=10, sticky='e')
    amount_entry = tk.Entry(form_frame, font=("Arial", 14), width=30)
    amount_entry.grid(row=2, column=1, padx=10, pady=10)

    tk.Button(form_frame, text="Salvar💾", command=lambda: save_transaction("saida", category_entry, description_entry, amount_entry), font=("Arial", 14)).grid(row=3, columnspan=2, pady=20)

    button_exit = tk.Button(root, text="❌", command=exit_app, width=3, height=1, font=("Arial", 14), bg='#9c0720', fg='white')
    button_exit.place(relx=1.0, rely=0.0, anchor='ne')  # Posiciona no canto superior direito

    button_back = tk.Button(root, text="⬅️", command=home_screen, width=3, height=1, font=("Arial", 14), bg='#00003d', fg='white')
    button_back.place(relx=0.0, rely=0.0, anchor='nw')  # Posiciona no canto superior esquerdo

# Salva a transação no banco de dados
def save_transaction(transaction_type, category_entry, description_entry, amount_entry):
    category = category_entry.get()
    description = description_entry.get()
    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor válido.")
        return

    if not category or not description:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return

    with sqlite3.connect('cashflow_system.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO transactions (type, category, description, amount) VALUES (?, ?, ?, ?)',
                       (transaction_type, category, description, amount))
        conn.commit()
        messagebox.showinfo("Sucesso", "Transação registrada com sucesso.")
        clear_fields([category_entry, description_entry, amount_entry])

# Tela de visualização do fluxo de caixa
def view_cashflow():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Fluxo de Caixa", font=("Georgia", 40, 'bold'), bg='#195074', fg='white').pack(pady=20)

    tree_frame = tk.Frame(root)
    tree_frame.pack(pady=20)

    columns = ('ID', 'Tipo', 'Categoria', 'Descrição', 'Valor')
    tree = ttk.Treeview(tree_frame, columns=columns, show='headings')
    tree.heading('ID', text='ID')
    tree.heading('Tipo', text='Tipo')
    tree.heading('Categoria', text='Categoria')
    tree.heading('Descrição', text='Descrição')
    tree.heading('Valor', text='Valor')

    tree.column('ID', width=30, anchor='center')
    tree.column('Tipo', width=100, anchor='center')
    tree.column('Categoria', width=250, anchor='center')
    tree.column('Descrição', width=300, anchor='center')
    tree.column('Valor', width=100, anchor='center')

    tree.pack()

    # Função para popular o Treeview
    def populate_treeview():
        # Limpa o Treeview
        for row in tree.get_children():
            tree.delete(row)
        # Busca as transações no banco de dados
        with sqlite3.connect('cashflow_system.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM transactions')
            for row in cursor.fetchall():
                color = 'white'
                if row[1] == 'entrada':
                    color = '#d0f5d3'  # Cor de fundo verde claro para entradas
                elif row[1] == 'saida':
                    color = '#fdd0d0'  # Cor de fundo vermelho claro para saídas
                tree.insert('', tk.END, values=row, tags=(color,))
                tree.tag_configure(color, background=color)

    populate_treeview()

    # Calcular o saldo final
    total_income = 0
    total_expense = 0
    with sqlite3.connect('cashflow_system.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT SUM(amount) FROM transactions WHERE type="entrada"')
        total_income = cursor.fetchone()[0] or 0
        cursor.execute('SELECT SUM(amount) FROM transactions WHERE type="saida"')
        total_expense = cursor.fetchone()[0] or 0

    final_balance = total_income - total_expense

    global final_balance_label
    final_balance_label = tk.Label(root, text=f"Saldo Final: R${final_balance:.2f}", font=("Arial", 24, 'bold'))
    final_balance_label.pack(pady=20)

    if final_balance > 0:
        final_balance_label.config(fg='green', font=("Arial", 24, 'bold'))
    elif final_balance < 0:
        final_balance_label.config(fg='#b71c1c', font=("Arial", 24, 'bold'))
    else:
        final_balance_label.config(fg='blue', font=("Arial", 24, 'bold'))

    button_back = tk.Button(root, text="⬅️", command=home_screen, width=3, height=1, font=("Arial", 14), bg='#00003d', fg='white')
    button_back.place(relx=0.0, rely=0.0, anchor='nw')  # Posiciona no canto superior esquerdo

    button_exit = tk.Button(root, text="❌", command=exit_app, width=3, height=1, font=("Arial", 14), bg='#9c0720', fg='white')
    button_exit.place(relx=1.0, rely=0.0, anchor='ne')  # Posiciona no canto superior direito

    # Botão de Excluir
    def delete_transaction():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Aviso", "Selecione uma transação para excluir.")
            return

        transaction_id = tree.item(selected_item[0], 'values')[0]
        with sqlite3.connect('cashflow_system.db') as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM transactions WHERE id=?', (transaction_id,))
            conn.commit()
            messagebox.showinfo("Sucesso", "Transação excluída com sucesso.")
            populate_treeview()
            update_balance()

    # Botão de Editar
    def edit_transaction():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Aviso", "Selecione uma transação para editar.")
            return

        transaction_id = tree.item(selected_item[0], 'values')[0]
        category = tree.item(selected_item[0], 'values')[2]
        description = tree.item(selected_item[0], 'values')[3]
        amount = tree.item(selected_item[0], 'values')[4]

        edit_window = tk.Toplevel(root)
        edit_window.title("Editar Transação")
        edit_window.geometry("400x300")

        tk.Label(edit_window, text="Categoria:", font=("Arial", 16)).grid(row=0, column=0, padx=10, pady=10, sticky='e')
        category_entry = tk.Entry(edit_window, font=("Arial", 14))
        category_entry.insert(0, category)
        category_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(edit_window, text="Descrição:", font=("Arial", 16)).grid(row=1, column=0, padx=10, pady=10, sticky='e')
        description_entry = tk.Entry(edit_window, font=("Arial", 14))
        description_entry.insert(0, description)
        description_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(edit_window, text="Valor:", font=("Arial", 16)).grid(row=2, column=0, padx=10, pady=10, sticky='e')
        amount_entry = tk.Entry(edit_window, font=("Arial", 14))
        amount_entry.insert(0, amount)
        amount_entry.grid(row=2, column=1, padx=10, pady=10)

        def update_transaction():
            new_category = category_entry.get()
            new_description = description_entry.get()
            try:
                new_amount = float(amount_entry.get())
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira um valor válido.")
                return

            if not new_category or not new_description:
                messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
                return

            with sqlite3.connect('cashflow_system.db') as conn:
                cursor = conn.cursor()
                cursor.execute('UPDATE transactions SET category=?, description=?, amount=? WHERE id=?',
                               (new_category, new_description, new_amount, transaction_id))
                conn.commit()
                messagebox.showinfo("Sucesso", "Transação atualizada com sucesso.")
                edit_window.destroy()
                populate_treeview()
                update_balance()

        tk.Button(edit_window, text="Salvar", command=update_transaction).grid(row=3, columnspan=2, pady=20)

    # Botão de Pesquisar
    def search_transactions():
        search_term = search_entry.get()
        for row in tree.get_children():
            tree.delete(row)

        with sqlite3.connect('cashflow_system.db') as conn:
            cursor = conn.cursor()
            query = 'SELECT * FROM transactions WHERE description LIKE ?'
            cursor.execute(query, ('%' + search_term + '%',))
            for row in cursor.fetchall():
                color = 'white'
                if row[1] == 'entrada':
                    color = '#d0f5d3'  # Cor de fundo verde claro para entradas
                elif row[1] == 'saida':
                    color = '#fdd0d0'  # Cor de fundo vermelho claro para saídas
                tree.insert('', tk.END, values=row, tags=(color,))
                tree.tag_configure(color, background=color)

    search_frame = tk.Frame(root)
    search_frame.pack(pady=20)

    tk.Label(search_frame, text="Pesquisar Descrição:", font=("Arial", 16)).pack(side=tk.LEFT, padx=10)
    search_entry = tk.Entry(search_frame, font=("Arial", 14))
    search_entry.pack(side=tk.LEFT, padx=10)
    tk.Button(search_frame, text="Pesquisar", command=search_transactions).pack(side=tk.LEFT, padx=10)

    tk.Button(root, text="Excluir", command=delete_transaction, font=("Arial", 14), bg='#f44336', fg='white').pack(side=tk.LEFT, padx=10)
    tk.Button(root, text="Editar", command=edit_transaction, font=("Arial", 14), bg='#4CAF50', fg='white').pack(side=tk.LEFT, padx=10)

# Atualiza o saldo final
def update_balance():
    total_income = 0
    total_expense = 0
    with sqlite3.connect('cashflow_system.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT SUM(amount) FROM transactions WHERE type="entrada"')
        total_income = cursor.fetchone()[0] or 0
        cursor.execute('SELECT SUM(amount) FROM transactions WHERE type="saida"')
        total_expense = cursor.fetchone()[0] or 0

    final_balance = total_income - total_expense

    global final_balance_label
    final_balance_label.config(text=f"Saldo Final: R${final_balance:.2f}")

    if final_balance > 0:
        final_balance_label.config(fg='green')
    elif final_balance < 0:
        final_balance_label.config(fg='#b71c1c')
    else:
        final_balance_label.config(fg='blue')

# Fecha o aplicativo
def exit_app():
    root.quit()

# Inicializa o banco de dados e a tela inicial
init_db()
root = tk.Tk()
root.title("Sistema de Fluxo de Caixa")
root.geometry("1200x800")
root.configure(bg='#195074')

start_screen()
root.mainloop()
