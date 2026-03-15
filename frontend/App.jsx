import React from 'react';
import { Mic, Send, Bot, ShieldCheck } from 'lucide-react';

function App() {
  return (
    <div className="min-h-screen bg-slate-50 flex flex-col items-center justify-center p-4">
      <header className="mb-8 text-center">
        <h1 className="text-4xl font-bold text-indigo-900 mb-2">NovaBridge</h1>
        <p className="text-slate-600">Voice-Powered Government Subsidy Assistant</p>
      </header>
      
      <main className="w-full max-w-lg bg-white rounded-2xl shadow-xl overflow-hidden">
        <div className="p-6 h-96 overflow-y-auto border-b border-slate-100 italic text-slate-400">
          "Welcome! How can I help you today?"
        </div>
        
        <div className="p-4 bg-slate-50 flex items-center gap-4">
          <button className="p-4 bg-indigo-600 text-white rounded-full hover:bg-indigo-700 transition-all shadow-lg">
            <Mic size={24} />
          </button>
          <input 
            type="text" 
            placeholder="Type your request here..." 
            className="flex-1 p-3 rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-indigo-500"
          />
          <button className="p-3 bg-slate-200 text-slate-600 rounded-xl hover:bg-slate-300 transition-all">
            <Send size={20} />
          </button>
        </div>
      </main>

      <footer className="mt-12 grid grid-cols-1 md:grid-cols-3 gap-6 text-sm text-slate-500 max-w-3xl">
        <div className="flex items-center gap-2">
          <Bot size={16} />
          <span>Powered by Amazon Nova 2</span>
        </div>
        <div className="flex items-center gap-2">
          <ShieldCheck size={16} />
          <span>Secure & Private</span>
        </div>
        <div className="text-center">
          <span>Hackathon MVP v0.1</span>
        </div>
      </footer>
    </div>
  );
}

export default App;
