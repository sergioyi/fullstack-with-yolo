import { useLocation, useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Download, ArrowLeft } from "lucide-react";
import { useToast } from "@/hooks/use-toast";

const Result = () => {
  const navigate = useNavigate();
  const { state } = useLocation();
  const { toast } = useToast();

  const pdfPath = state?.pdfPath;

  const handleDownload = () => {
    if (!pdfPath) {
      toast({
        title: "Erro",
        description: "Nenhum arquivo disponível para download.",
        variant: "destructive",
      });
      return;
    }

    toast({
      title: "Download iniciado",
      description: "O relatório está sendo baixado...",
    });

    // Simular o download do arquivo (substituir pelo download real)
    const link = document.createElement("a");
    link.href = pdfPath; // Substitua pelo caminho real do PDF
    link.download = "Relatorio.pdf";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
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
              <h2 className="text-xl font-semibold text-gray-900 mb-2">Análise Concluída!</h2>
              <p className="text-gray-600 text-sm">
                Abaixo segue em PDF o resultado da análise da imagem.
              </p>
            </div>

            <div className="border border-gray-200 rounded-lg p-4 bg-gray-50">
              <div className="flex items-center space-x-3">
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
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

export default Result;
