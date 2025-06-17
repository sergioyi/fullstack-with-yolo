import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

const Loading = () => {
  const navigate = useNavigate();

  useEffect(() => {
    // Simula o tempo de processamento (5 segundos)
    const timeout = setTimeout(() => {
      navigate("/resultado"); // redireciona para página de resultado
    }, 5000);

    return () => clearTimeout(timeout); // limpa o timeout se o componente desmontar
  }, [navigate]);

  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center px-4">
      <div className="text-center space-y-8">
        <h1 className="text-3xl font-light text-[#007AFF] mb-8">
          Analisando os dados enviados...
        </h1>

        <div className="flex items-center justify-center">
          <div className="relative">
            {/* Círculo de progresso */}
            <svg className="w-20 h-20 transform -rotate-90" viewBox="0 0 80 80">
              <circle
                cx="40"
                cy="40"
                r="30"
                stroke="currentColor"
                strokeWidth="8"
                fill="transparent"
                className="text-gray-200"
              />
              <circle
                cx="40"
                cy="40"
                r="30"
                stroke="currentColor"
                strokeWidth="8"
                fill="transparent"
                strokeDasharray={`${2 * Math.PI * 30}`}
                strokeDashoffset={`${2 * Math.PI * 30 * 0.25}`}
                className="text-[#007AFF] transition-all duration-1000 ease-in-out animate-pulse"
                strokeLinecap="round"
              />
            </svg>

            {/* Ponto animado */}
            <div className="absolute inset-0 flex items-center justify-center">
              <div className="w-3 h-3 bg-[#007AFF] rounded-full animate-ping"></div>
            </div>
          </div>
        </div>

        <div className="space-y-2">
          <div className="flex justify-center space-x-1">
            <div
              className="w-2 h-2 bg-[#007AFF] rounded-full animate-bounce"
              style={{ animationDelay: "0ms" }}
            ></div>
            <div
              className="w-2 h-2 bg-[#007AFF] rounded-full animate-bounce"
              style={{ animationDelay: "150ms" }}
            ></div>
            <div
              className="w-2 h-2 bg-[#007AFF] rounded-full animate-bounce"
              style={{ animationDelay: "300ms" }}
            ></div>
          </div>
          <p className="text-gray-600 text-sm">Processando sua solicitação...</p>
        </div>
      </div>
    </div>
  );
};

export default Loading;
