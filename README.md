# salu-exam
Repositorio para o projeto solicitado pela rede de saúde Salú
## Como o Código Funciona

O projeto está organizado em módulos que colaboram para realizar o agendamento de maneira clara e testável:

1. **exam_type_enum.py**  
   Define o `Enum` `ExamTypeEnum` com todos os tipos de exame disponíveis na rede de clínicas.

2. **models.py**  
   - `Clinic`: representa cada unidade da rede, armazenando `clinic_id`, nome, horário de funcionamento (`open_time` e `close_time`), lista de exames suportados e os agendamentos já realizados.  
   - `Exam`: representa um exame agendado, armazena `employee_id`, `clinic_id`, tipo de exame e horário de início/fim (1 hora). Tem o método `overlaps(other)` para detectar sobreposição de horários dentro da mesma clínica.

3. **data_store.py**  
   Implementa o singleton `DataStore`, que mantém em memória todas as clínicas.  
   - `initialize_sample_data()`: popula duas clínicas de exemplo com horários e tipos de exame.  
   - `get_clinic(id)`, `add_clinic(clinic)`: para buscar e cadastrar clínicas.

4. **exam_scheduler.py**  
   - **Construtor**: instancia o `DataStore` e, se não houver clínicas cadastradas, chama `initialize_sample_data()`.  
   - **Método `execute(employee_id, clinic_id, exam_type, exam_start)`**:  
     1. Busca a clínica pelo `clinic_id`. Se não existir, retorna erro.  
     2. Verifica se o `exam_type` está em `clinic.supported_exams`.  
     3. Confere se `exam_start` + 1h está dentro de `open_time` e `close_time`.  
     4. Cria um objeto `Exam` e percorre `clinic.scheduled_exams`; se `new_exam.overlaps(existing)` for `True`, bloqueia por conflito.  
     5. Se tudo passar, adiciona `new_exam` a `clinic.scheduled_exams` e retorna `(True, "Exame agendado com sucesso")`; senão, retorna `(False, mensagem_de_erro)`.

5. **`__main__.py`**  
   - Instancia `ExamSchedulerClass`.  
   - Lista as clínicas disponíveis (ID, nome e horário).  
   - Define parâmetros de exemplo (funcionário, clínica escolhida, tipo e horário).  
   - Chama `execute()` e imprime o resultado no console.

Esse fluxo modular facilita:  
- **Manutenção** (cada responsabilidade está em seu módulo),  
- **Testes unitários** (você pode, por exemplo, injetar clínicas no `DataStore` e testar apenas `execute()`),  
- **Extensão futura** (basta oferecer novos tipos de exame ou múltiplos horários).  
