
function [kHat,sigmaHat] = gpd(y)

%y = [0.3,0.4,0.3,0.3,0.5,0.6,0.2,0.3,0.3,0.5];
y;
paramEsts = gpfit(y);
kHat      = paramEsts(1)  ; % Tail index parameter
sigmaHat  = paramEsts(2) ;  % Scale parameter

end
