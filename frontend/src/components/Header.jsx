export default function Header() {
  return (
    <header className="flex items-baseline justify-between">
      <h1 className="text-3xl font-semibold tracking-tight">
        <span className="text-sky-400">FastAPI</span>{" "}
        <span className="text-slate-100">Todo</span>
      </h1>
    </header>
  );
}
