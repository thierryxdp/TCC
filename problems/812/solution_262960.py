def RemoverPalavras(Frase,Palavra_Remover:String): String;
Var
  Aux: str;
begin
  Aux := ´ ´ + Frase + ´ ´;
  Aux := StringReplace(Aux,´ ´+Palavra_Remover+´ ´,´ ´,[rfReplaceAll]);
  Result := Copy(Aux,2,Length(Aux)-1);
end;
 
procedure TForm1.Button1Click(Sender: TObject);
begin
  Edit2.Text := RemoverPalavras(Edit1.Text,´as´);
end;