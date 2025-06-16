
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { LogIn } from "lucide-react";
import { useToast } from "@/hooks/use-toast";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();
  const { toast } = useToast();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);

    // Simula autenticação
    setTimeout(() => {
      if (email && password) {
        toast({
          title: "Login realizado com sucesso!",
          description: "Redirecionando para a página sobre...",
        });
        navigate("/about");
      } else {
        toast({
          title: "Erro no login",
          description: "Por favor, preencha todos os campos.",
          variant: "destructive",
        });
      }
      setIsLoading(false);
    }, 1500);
  };

  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center px-4">
      <div className="w-full max-w-md space-y-8">
        <div className="text-center">
          <h1 className="text-4xl font-light text-[#007AFF] mb-8">Acesso ao Yolo AVC Analyze</h1>
        </div>

        <form onSubmit={handleLogin} className="space-y-6">
          <div className="space-y-2">
            <Label htmlFor="email" className="text-sm text-gray-600">
              E-mail
            </Label>
            <Input
              id="email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full px-3 py-3 bg-gray-200 border-0 rounded-md focus:bg-white focus:ring-2 focus:ring-[#007AFF] transition-all"
              required
            />
          </div>

          <div className="space-y-2">
            <Label htmlFor="password" className="text-sm text-gray-600">
              Password
            </Label>
            <Input
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full px-3 py-3 bg-gray-200 border-0 rounded-md focus:bg-white focus:ring-2 focus:ring-[#007AFF] transition-all"
              required
            />
          </div>

          {/* <div className="text-left">
            <button
              type="button"
              className="text-[#007AFF] text-sm hover:underline focus:outline-none"
              onClick={() => toast({ title: "Funcionalidade em desenvolvimento" })}
            >
              Forgot your password?
            </button>
          </div> */}

          <Button
            type="submit"
            disabled={isLoading}
            className="w-full bg-[#007AFF] hover:bg-[#0056CC] text-white py-3 rounded-md font-medium transition-colors"
          >
            {isLoading ? (
              <div className="flex items-center space-x-2">
                <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                <span>Entrando...</span>
              </div>
            ) : (
              <div className="flex items-center space-x-2">
                <LogIn size={20} />
                <span>Login</span>
              </div>
            )}
          </Button>
        </form>
      </div>
    </div>
  );
};

export default Login;
