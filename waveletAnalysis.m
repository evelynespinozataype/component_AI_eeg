%% Grafico 4 emociones con diferentes ondas
%%

clc;
clear;
close all;

%function to get the file name
S=22; %num of files
X=1;
wave = 10; % obs 1, time 2,Delta	3, Theta	4, Alpha1	5, Alpha2	6, Beta1	7,
%Beta2	8, Gamma1	9, Gamma2	10, Attention	11, Meditation 12
%namecolum = 'Theta';
namewave ='';
if wave==3 
    namewave ='Delta';
end
if wave==4 
    namewave ='Theta';
end
if wave==5 
    namewave ='Alpha';
end
if wave==7 
    namewave ='Beta';
end
if wave==8 
    namewave ='Beta';
end
if wave==9 
    namewave ='Gamma';
end
if wave==10 
    namewave ='Gamma';
end

arrayname_A = string.empty;
arrayname_M = string.empty;
arrayname_N = string.empty;
arrayname_T = string.empty;

for c=X:S
    if c<10
        arrayname_A(c) = strcat('0',string(c),'_A.csv');
        arrayname_M(c) = strcat('0',string(c),'_M.csv');
        arrayname_N(c) = strcat('0',string(c),'_N.csv');
        arrayname_T(c) = strcat('0',string(c),'_T.csv');
        fprintf(arrayname_A(c));
        fprintf(arrayname_M(c));
        fprintf(arrayname_N(c));
        fprintf(arrayname_T(c));
    end
    if c>=10
        arrayname_A(c) = strcat(string(c),'_A.csv');
        arrayname_M(c) = strcat(string(c),'_M.csv');
        arrayname_N(c) = strcat(string(c),'_N.csv');
        arrayname_T(c) = strcat(string(c),'_T.csv');
        fprintf(arrayname_A(c));
        fprintf(arrayname_M(c));
        fprintf(arrayname_N(c));
        fprintf(arrayname_T(c));
    end
end

%dt_median_usu = zeros();
for c=X:S
    % Function to read the files
    dt_usu_happ = table2array(readtable(strcat('data/',arrayname_A(c))));
    dt_usu_fear = table2array(readtable(strcat('data/',arrayname_M(c))));
    dt_usu_ange = table2array(readtable(strcat('data/',arrayname_N(c))));
    dt_usu_sad = table2array(readtable(strcat('data/',arrayname_T(c))));
    
    %init with 0
    dt_usu_happ(isnan(dt_usu_happ))=0;
    dt_usu_fear(isnan(dt_usu_fear))=0;
    dt_usu_ange(isnan(dt_usu_ange))=0;
    dt_usu_sad(isnan(dt_usu_sad))=0;
    
    %%TRANFORMER FOURIER
    F_happ = fft(dt_usu_happ(:,wave));
    F_happ = abs(F_happ);
    F_happ = F_happ/max(F_happ);
%     F_happ2 = fft(dt_usu_happ(:,wave+1));
%     F_happ2 = abs(F_happ2);
%     F_happ2 = F_happ2/max(F_happ2);

    F_fear = fft(dt_usu_fear(:,wave));
    F_fear = abs(F_fear);
    F_fear = F_fear/max(F_fear);
%     F_fear2 = fft(dt_usu_fear(:,wave+1));
%     F_fear2 = abs(F_fear2);
%     F_fear2 = F_fear2/max(F_fear2);

    F_ange = fft(dt_usu_ange(:,wave));
    F_ange = abs(F_ange);
    F_ange = F_ange/max(F_ange);
%     F_ange2 = fft(dt_usu_ange(:,wave+1));
%     F_ange2 = abs(F_ange2);
%     F_ange2 = F_ange2/max(F_ange2);

    F_sad = fft(dt_usu_sad(:,wave));
    F_sad = abs(F_sad);
    F_sad = F_sad/max(F_sad);
%     F_sad2 = fft(dt_usu_sad(:,wave+1));
%     F_sad2 = abs(F_sad2);
%     F_sad2 = F_sad2/max(F_sad2);

    F_happ(isempty(F_happ))=0;
    F_fear(isempty(F_fear))=0;
    F_ange(isempty(F_ange))=0;
    F_sad(isempty(F_sad))=0;

    % GETTING Amplitud and frequency
    if length(F_happ)>3
        [dt_amp_happPRO,dt_fre_happPRO] = findpeaks(F_happ, "MinPeakProminence",0);
        [dt_amp_happDIS,dt_fre_happDIS] = findpeaks(F_happ, "MinPeakDistance",0);
    end
    if length(F_fear)>3
        [dt_amp_fearPRO,dt_fre_fearPRO] = findpeaks(F_fear, "MinPeakProminence",0);
        [dt_amp_fearDIS,dt_fre_fearDIS] = findpeaks(F_fear, "MinPeakDistance",0);
    end
    if length(F_ange)>3
        [dt_amp_angePRO,dt_fre_angePRO] = findpeaks(F_ange, "MinPeakProminence",0);
        [dt_amp_angeDIS,dt_fre_angeDIS] = findpeaks(F_ange, "MinPeakDistance",0);
    end
    if length(F_sad)>3
        [dt_amp_sadPRO,dt_fre_sadPRO] = findpeaks(F_sad, "MinPeakProminence",0);
        [dt_amp_sadDIS,dt_fre_sadDIS] = findpeaks(F_sad, "MinPeakDistance",0);
    end
    
%   Happ
    count_amp_peak_happ = length(dt_amp_happPRO);
    count_fre_peak_happ = length(dt_amp_happDIS);
    rms_peak_happ = round(peak2rms(F_happ),2);
    peak2peak_happ = round(peak2peak(F_happ),2);
    %fear
    count_amp_peak_fear = length(dt_amp_fearPRO);
    count_fre_peak_fear = length(dt_amp_fearDIS);
    rms_peak_fear = round(peak2rms(F_fear),2);
    peak2peak_fear = round(peak2peak(F_fear),2);
    %ange
    count_amp_peak_ange = length(dt_amp_angePRO);
    count_fre_peak_ange = length(dt_amp_angeDIS);
    rms_peak_ange = round(peak2rms(F_ange),2);
    peak2peak_ange = round(peak2peak(F_ange),2);
    %sad
    count_amp_peak_sad = length(dt_amp_sadPRO);
    count_fre_peak_sad = length(dt_amp_sadDIS);
    rms_peak_sad = round(peak2rms(F_sad),2);
    peak2peak_sad = round(peak2peak(F_sad),2);
   
    %entropy_happ = entropy(F_happ);

%     fprintf(string(length(dt_fre_happ)));
%     fprintf(string(length(F_happ)));

%     fre_median_happ =  length(dt_fre_happ)/length(F_happ);
%     fre_median_fear = length(dt_fre_fear)/length(F_fear);
%     fre_median_ange = length(dt_fre_ange)/length(F_ange);
%     fre_median_sad = length(dt_fre_sad)/length(F_sad);
   
     dt_TOTAL_happ(c,:) = table(c,count_amp_peak_happ, count_fre_peak_happ, rms_peak_happ, peak2peak_happ);
     dt_TOTAL_fear(c,:) = table(c,count_amp_peak_fear, count_fre_peak_fear, rms_peak_fear, peak2peak_fear);
     dt_TOTAL_ange(c,:) = table(c,count_amp_peak_ange, count_fre_peak_ange, rms_peak_ange, peak2peak_ange);
     dt_TOTAL_sad(c,:) = table(c,count_amp_peak_sad, count_fre_peak_sad, rms_peak_sad, peak2peak_sad);
    
%     nexttile
%     hold on
%     plot(F_happ);
%     findpeaks(F_happ, "MinPeakProminence",0.2);
%   % findpeaks(normalize(dt_usu_happ(:,9),"range"), "MinPeakProminence",0.2);
% %     plot(F_happ2);
%     %findpeaks(F_happ, "MinPeakDistance",0);
%     title(strcat('Happiness u',string(c),namewave));
%     hold off
% 
%     nexttile
%     hold on
%     plot(F_fear);
%     findpeaks(F_fear, "MinPeakProminence",0.2);
% %     plot(F_fear2);
% %     findpeaks(F_fear, "MinPeakDistance",2);
%     title(strcat('Fear u',string(c),namewave));
%     hold off
% 
%     nexttile
%     hold on
%     plot(F_ange);
%     findpeaks(F_ange, "MinPeakProminence",0.2);
% %     plot(F_ange2);
% %     findpeaks(F_ange, "MinPeakDistance",2);
%     title(strcat('Anger u',string(c),namewave));
%     hold off
% 
%     nexttile
%     hold on
%     plot(F_sad);
%     findpeaks(F_sad, "MinPeakProminence",0.2);
% %     plot(F_sad2);
% %     findpeaks(F_sad, "MinPeakDistance",2);
%     title(strcat('Sad u',string(c),namewave));
%     hold off

end 