
import { useState, useRef } from "react";
import { useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Upload } from "lucide-react";
import { useToast } from "@/hooks/use-toast";

const About = () => {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [isDragging, setIsDragging] = useState(false);
  const fileInputRef = useRef<HTMLInputElement>(null);
  const navigate = useNavigate();
  const { toast } = useToast();

  const handleFileSelect = (file: File) => {
    if (file.type === "application/pdf" || file.type.startsWith("image/")) {
      setSelectedFile(file);
      toast({
        title: "Arquivo selecionado",
        description: `${file.name} foi selecionado com sucesso.`,
      });
    } else {
      toast({
        title: "Tipo de arquivo não suportado",
        description: "Por favor, selecione um arquivo PDF ou imagem.",
        variant: "destructive",
      });
    }
  };

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
    const files = e.dataTransfer.files;
    if (files.length > 0) {
      handleFileSelect(files[0]);
    }
  };

  const handleFileInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const files = e.target.files;
    if (files && files.length > 0) {
      handleFileSelect(files[0]);
    }
  };

  const handleContinue = () => {
    if (selectedFile) {
      navigate("/loading");
    } else {
      toast({
        title: "Nenhum arquivo selecionado",
        description: "Por favor, selecione um arquivo antes de continuar.",
        variant: "destructive",
      });
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center px-4">
      <div className="w-full max-w-md space-y-8">
        <div className="text-center">
          <h1 className="text-4xl font-light text-[#007AFF] mb-8">Yolo AVC Analyze</h1>
        </div>

        <div className="space-y-6">
          <div>
            <h2 className="text-xl font-semibold text-gray-900 mb-4">Sobre</h2>
            <p className="text-gray-600 text-sm leading-relaxed">
            Yolo AVC Analyze é sistema de apoio ao diagnóstico médico para detectar sinais de AVC em imagens de tomografia. O sistema processa as imagens em tempo real, gerando relatórios destacando possíveis áreas afetadas, auxiliando profissionais da saúde na tomada de decisão rápida e eficaz.
            </p>
          </div>

          <div>
            <h3 className="text-lg font-medium text-gray-900 mb-4">Envio de arquivo</h3>
            
            <div
              className={`relative border-2 border-dashed rounded-lg p-8 text-center transition-colors ${
                isDragging
                  ? "border-[#007AFF] bg-blue-50"
                  : selectedFile
                  ? "border-green-400 bg-green-50"
                  : "border-gray-300 bg-white"
              }`}
              onDragOver={handleDragOver}
              onDragLeave={handleDragLeave}
              onDrop={handleDrop}
              onClick={() => fileInputRef.current?.click()}
            >
              <input
                ref={fileInputRef}
                type="file"
                className="hidden"
                accept=".pdf,image/*"
                onChange={handleFileInputChange}
              />
              
              <Upload className="mx-auto h-12 w-12 text-gray-400 mb-4" />
              
              {selectedFile ? (
                <div>
                  <p className="text-green-600 font-medium">{selectedFile.name}</p>
                  <p className="text-sm text-gray-500 mt-1">
                    {(selectedFile.size / 1024 / 1024).toFixed(2)} MB
                  </p>
                </div>
              ) : (
                <div>
                  <p className="text-gray-600 mb-2">Clique ou arraste o arquivo para esta área para fazer upload</p>
                  <p className="text-sm text-gray-400">Arquivos de imagem</p>
                </div>
              )}
            </div>
          </div>

          <div className="flex space-x-4">
            <Button
              variant="outline"
              onClick={() => navigate("/login")}
              className="flex-1 border-gray-300 text-gray-700 hover:bg-gray-50"
            >
              Cancel
            </Button>
            <Button
              onClick={handleContinue}
              disabled={!selectedFile}
              className="flex-1 bg-[#007AFF] hover:bg-[#0056CC] text-white"
            >
              Continue
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default About;
