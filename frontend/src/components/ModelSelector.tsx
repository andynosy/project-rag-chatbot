import React from 'react';

interface Model {
  id: string;
  name: string;
  provider: string;
}

interface Props {
  models: Model[];
  selectedModel: string;
  onSelect: (modelId: string) => void;
}

export const ModelSelector: React.FC<Props> = ({ models, selectedModel, onSelect }) => {
  return (
    <div className="flex items-center space-x-2">
      <label htmlFor="model-select" className="font-medium text-gray-700">
        Model:
      </label>
      <select
        id="model-select"
        value={selectedModel}
        onChange={(e) => onSelect(e.target.value)}
        className="block w-full max-w-xs rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
      >
        {models.map((model) => (
          <option key={model.id} value={model.id}>
            {model.name} ({model.provider})
          </option>
        ))}
      </select>
    </div>
  );
}