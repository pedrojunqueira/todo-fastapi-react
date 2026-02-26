export default function TodoItem({ todo, deleteTodo, toggleTodo }) {
  return (
    <li className="flex items-center justify-between gap-3 rounded-lg bg-slate-900/40 px-3 py-2 text-sm border border-slate-700">
      <label className="flex items-center gap-2 flex-1">
        <input
          type="checkbox"
          checked={todo.completed}
          onChange={() => toggleTodo(todo)}
          className="h-4 w-4 rounded border-slate-600 text-sky-500 focus:ring-sky-500"
        />
        <span
          className={`${
            todo.completed ? "line-through text-slate-500" : "text-slate-100"
          }`}
        >
          {todo.text}
        </span>
      </label>
      <button
        onClick={() => deleteTodo(todo.id)}
        className="text-xs text-red-300 hover:text-red-200"
      >
        Delete
      </button>
    </li>
  );
}
