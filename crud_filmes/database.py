import sqlite3
import os
from typing import List, Tuple, Optional

class DatabaseManager:
    def __init__(self, db_name: str = "filmes.db"):
        self.db_name = db_name
        self._initialize_database()
    
    def _initialize_database(self):
        """Inicializa o banco de dados e cria a tabela se não existir"""
        try:
            # Conecta ao banco (cria o arquivo se não existir)
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                
                # Verifica se a tabela já existe
                cursor.execute("""
                    SELECT name FROM sqlite_master 
                    WHERE type='table' AND name='filmes'
                """)
                
                if not cursor.fetchone():
                    print("📋 Criando tabela 'filmes'...")
                    self._create_table(conn)
                else:
                    print("✅ Tabela 'filmes' já existe!")
                    
        except Exception as e:
            print(f"❌ Erro ao inicializar banco: {e}")
            # Tenta recriar o banco se der erro
            self._recreate_database()
    
    def _create_table(self, conn):
        """Cria a tabela filmes"""
        try:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE filmes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    genero TEXT NOT NULL,
                    ano INTEGER NOT NULL
                )
            ''')
            conn.commit()
            print("✅ Tabela 'filmes' criada com sucesso!")
            
            # Adiciona alguns filmes de exemplo
            self._add_sample_data(conn)
            
        except Exception as e:
            print(f"❌ Erro ao criar tabela: {e}")
    
    def _add_sample_data(self, conn):
        """Adiciona alguns filmes de exemplo"""
        try:
            cursor = conn.cursor()
            sample_filmes = [
                ("Matrix", "Ficção Científica", 1999),
                ("O Poderoso Chefão", "Drama", 1972),
                ("Toy Story", "Animação", 1995),
                ("Interestelar", "Ficção Científica", 2014),
                ("Forrest Gump", "Drama", 1994)
            ]
            
            cursor.executemany(
                "INSERT INTO filmes (titulo, genero, ano) VALUES (?, ?, ?)",
                sample_filmes
            )
            conn.commit()
            print(f"✅ {len(sample_filmes)} filmes de exemplo adicionados!")
            
        except Exception as e:
            print(f"❌ Erro ao adicionar dados de exemplo: {e}")
    
    def _recreate_database(self):
        """Recria o banco de dados do zero"""
        try:
            # Remove o arquivo corrompido se existir
            if os.path.exists(self.db_name):
                os.remove(self.db_name)
                print("🗑️ Arquivo corrompido removido.")
            
            # Cria novo banco
            print("🔄 Recriando banco de dados...")
            self._initialize_database()
            
        except Exception as e:
            print(f"❌ Erro ao recriar banco: {e}")
    
    def adicionar_filme(self, titulo: str, genero: str, ano: int) -> int:
        """Adiciona um novo filme"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO filmes (titulo, genero, ano) VALUES (?, ?, ?)",
                    (titulo, genero, ano)
                )
                conn.commit()
                print(f"✅ Filme '{titulo}' adicionado com ID: {cursor.lastrowid}")
                return cursor.lastrowid
        except Exception as e:
            print(f"❌ Erro ao adicionar filme: {e}")
            return -1
    
    def listar_filmes(self, busca: str = None) -> List[Tuple]:
        """Lista todos os filmes"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                if busca:
                    cursor.execute(
                        "SELECT * FROM filmes WHERE titulo LIKE ? ORDER BY titulo",
                        (f"%{busca}%",)
                    )
                else:
                    cursor.execute("SELECT * FROM filmes ORDER BY titulo")
                
                filmes = cursor.fetchall()
                print(f"✅ {len(filmes)} filmes encontrados!")
                return filmes
                
        except Exception as e:
            print(f"❌ Erro ao listar filmes: {e}")
            return []
    
    def obter_filme(self, filme_id: int) -> Optional[Tuple]:
        """Obtém um filme específico"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM filmes WHERE id = ?", (filme_id,))
                filme = cursor.fetchone()
                if filme:
                    print(f"✅ Filme ID {filme_id} encontrado!")
                else:
                    print(f"⚠️ Filme ID {filme_id} não encontrado!")
                return filme
        except Exception as e:
            print(f"❌ Erro ao obter filme: {e}")
            return None
    
    def editar_filme(self, filme_id: int, titulo: str, genero: str, ano: int) -> bool:
        """Edita um filme"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE filmes SET titulo = ?, genero = ?, ano = ? WHERE id = ?",
                    (titulo, genero, ano, filme_id)
                )
                conn.commit()
                success = cursor.rowcount > 0
                if success:
                    print(f"✅ Filme ID {filme_id} atualizado!")
                else:
                    print(f"⚠️ Filme ID {filme_id} não encontrado!")
                return success
        except Exception as e:
            print(f"❌ Erro ao editar filme: {e}")
            return False
    
    def deletar_filme(self, filme_id: int) -> bool:
        """Exclui um filme"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM filmes WHERE id = ?", (filme_id,))
                conn.commit()
                success = cursor.rowcount > 0
                if success:
                    print(f"✅ Filme ID {filme_id} excluído!")
                else:
                    print(f"⚠️ Filme ID {filme_id} não encontrado!")
                return success
        except Exception as e:
            print(f"❌ Erro ao excluir filme: {e}")
            return False

# Teste do banco
if __name__ == "__main__":
    print("🧪 Testando banco de dados...")
    db = DatabaseManager()
    
    # Testar operações
    filmes = db.listar_filmes()
    print("🎬 Filmes no banco:", filmes)
    
    print("✅ Banco testado com sucesso!")