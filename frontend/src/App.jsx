import Header from "./components/Header";
import CreateTodo from "./components/CreateTodo";
import Todos from "./components/Todos";
import TodoItem from "./components/TodoItem";
import { TodoProvider } from "./context/TodoProvider";
import { useTodo } from "./hooks/useTodo";

function AppContent() {
  const { todos, loading, error, addTodo, removeTodo, toggleTodo } = useTodo();

  return (
    <div className="p-4 min-h-screen bg-slate-900 text-slate-100 flex items-start justify-center">
      <div className="w-full max-w-xl bg-slate-800/80 rounded-2xl shadow-xl border border-slate-700 space-y-6 p-6">
        <Header />
        {error && <p className="text-red-400 text-sm">{error}</p>}
        <CreateTodo addTodo={addTodo} />
        <Todos>
          {loading ? (
            <p className="text-slate-400 text-sm">Loading...</p>
          ) : (
            todos.map((todo) => (
              <TodoItem
                key={todo.id}
                todo={todo}
                deleteTodo={removeTodo}
                toggleTodo={toggleTodo}
              />
            ))
          )}
        </Todos>
      </div>
    </div>
  );
}

function App() {
  return (
    <TodoProvider>
      <AppContent />
    </TodoProvider>
  );
}

export default App;
