
import { useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Download, ArrowLeft } from "lucide-react";
import { useToast } from "@/hooks/use-toast";

const Result = () => {
  const navigate = useNavigate();
  const { toast } = useToast();

  const handleDownload = () => {
    toast({
      title: "Download iniciado",
      description: "O relatório está sendo baixado...",
    });
    // Aqui seria implementado o download real do arquivo
  };

  const handleNewAnalysis = () => {
    navigate("/about");
  };

  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center px-4">
      <div className="w-full max-w-md space-y-8">
        <div className="text-center">
          <h1 className="text-4xl font-light text-[#007AFF] mb-8">Resultado</h1>
        </div>

        <Card className="bg-white shadow-sm border border-gray-200">
          <CardContent className="p-6 space-y-6">
            <div className="text-center space-y-4">
              <div className="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto">
                <svg className="w-8 h-8 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                </svg>
              </div>
              
              <div>
                <h2 className="text-xl font-semibold text-gray-900 mb-2">Análise Concluída!</h2>
                <p className="text-gray-600 text-sm">
                  Abaixo segue em PDF o resultado da análise da imagem.
                </p>
              </div>
            </div>

            <div className="border border-gray-200 rounded-lg p-4 bg-gray-50">
              <div className="flex items-center space-x-3">
                <div className="w-10 h-10 bg-red-100 rounded flex items-center justify-center">
                  <svg className="w-5 h-5 text-red-600" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4zm2 6a1 1 0 011-1h6a1 1 0 110 2H7a1 1 0 01-1-1zm1 3a1 1 0 100 2h6a1 1 0 100-2H7z" clipRule="evenodd" />
                  </svg>
                </div>
                <div className="flex-1">
                  <p className="font-medium text-gray-900">Relatório do resultado</p>
                  <p className="text-sm text-gray-500">PDF • 2.4 MB</p>
                </div>
                <Button
                  size="sm"
                  onClick={handleDownload}
                  className="bg-[#007AFF] hover:bg-[#0056CC] text-white"
                >
                  <Download size={16} className="mr-1" />
                  Download
                </Button>
              </div>
            </div>

            <div className="space-y-3">
              <Button
                onClick={handleNewAnalysis}
                className="w-full bg-[#007AFF] hover:bg-[#0056CC] text-white"
              >
                Nova Análise
              </Button>
              
              <Button
                variant="outline"
                onClick={() => navigate("/login")}
                className="w-full border-gray-300 text-gray-700 hover:bg-gray-50"
              >
                <ArrowLeft size={16} className="mr-2" />
                Voltar ao Início
              </Button>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

export default Result;
