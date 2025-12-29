// ==========================================
// DEEP SPACE FUSION - AI OPERATIONS DASHBOARD
// Advanced Interactive MLOps Interface
// ==========================================

// === GLOBAL STATE ===
const state = {
    currentTab: 'overview',
    currentChart: null,
    colorSchemes: {
        violet: ['#8B5CF6', '#6366F1', '#A855F7'],
        cyan: ['#00F0FF', '#0EA5E9', '#06B6D4'],
        purple: ['#A855F7', '#EC4899', '#8B5CF6'],
        green: ['#10B981', '#059669', '#34D399'],
        orange: ['#F59E0B', '#EF4444', '#FB923C']
    },
    charts: {},
    animations: {},
    particles: []
};

// === INITIALIZATION ===
document.addEventListener('DOMContentLoaded', () => {
    initializeParticles();
    initializeNavigation();
    initializeTabs();
    initializeCharts();
    initializeCounters();
    initializeDynamicTitles();
    initializeColorPickers();
    initializeInteractions();
    startRealTimeUpdates();
});

// === PARTICLE BACKGROUND ===
function initializeParticles() {
    const canvas = document.getElementById('particleCanvas');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    
    // Create particles
    for (let i = 0; i < 100; i++) {
        state.particles.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            vx: (Math.random() - 0.5) * 0.5,
            vy: (Math.random() - 0.5) * 0.5,
            radius: Math.random() * 2 + 1,
            opacity: Math.random() * 0.5 + 0.2
        });
    }
    
    function animateParticles() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        state.particles.forEach((particle, i) => {
            // Update position
            particle.x += particle.vx;
            particle.y += particle.vy;
            
            // Boundary check
            if (particle.x < 0 || particle.x > canvas.width) particle.vx *= -1;
            if (particle.y < 0 || particle.y > canvas.height) particle.vy *= -1;
            
            // Draw particle
            ctx.beginPath();
            ctx.arc(particle.x, particle.y, particle.radius, 0, Math.PI * 2);
            ctx.fillStyle = `rgba(139, 92, 246, ${particle.opacity})`;
            ctx.fill();
            
            // Draw connections
            state.particles.forEach((otherParticle, j) => {
                if (i !== j) {
                    const dx = particle.x - otherParticle.x;
                    const dy = particle.y - otherParticle.y;
                    const distance = Math.sqrt(dx * dx + dy * dy);
                    
                    if (distance < 100) {
                        ctx.beginPath();
                        ctx.moveTo(particle.x, particle.y);
                        ctx.lineTo(otherParticle.x, otherParticle.y);
                        ctx.strokeStyle = `rgba(0, 240, 255, ${0.1 * (1 - distance / 100)})`;
                        ctx.lineWidth = 0.5;
                        ctx.stroke();
                    }
                }
            });
        });
        
        requestAnimationFrame(animateParticles);
    }
    
    animateParticles();
    
    // Resize handler
    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });
}

// === NAVIGATION ===
function initializeNavigation() {
    updateTime();
    setInterval(updateTime, 1000);
    
    // Settings button
    const settingsBtn = document.getElementById('settingsBtn');
    if (settingsBtn) {
        settingsBtn.addEventListener('click', () => {
            alert('Settings panel coming soon!');
        });
    }
}

function updateTime() {
    const timeElement = document.getElementById('navTime');
    if (!timeElement) return;
    
    const now = new Date();
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');
    timeElement.textContent = `${hours}:${minutes}:${seconds}`;
}

// === TAB SYSTEM ===
function initializeTabs() {
    const tabButtons = document.querySelectorAll('.tab-btn');
    
    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            const tabName = button.getAttribute('data-tab');
            switchTab(tabName);
        });
    });
}

function switchTab(tabName) {
    // Update buttons
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    document.querySelector(`[data-tab="${tabName}"]`).classList.add('active');
    
    // Update content
    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.remove('active');
    });
    document.getElementById(tabName).classList.add('active');
    
    state.currentTab = tabName;
    
    // Reinitialize charts for the new tab
    setTimeout(() => {
        initializeChartsForTab(tabName);
    }, 100);
}

// === DYNAMIC TITLES ===
function initializeDynamicTitles() {
    const titles = [
        'AI OPERATIONS',
        'MLOPS CONTROL',
        'DEEP SPACE FUSION',
        'NEURAL NEXUS',
        'QUANTUM INSIGHTS'
    ];
    
    let currentIndex = 0;
    const mainTitle = document.getElementById('mainTitle');
    
    setInterval(() => {
        currentIndex = (currentIndex + 1) % titles.length;
        mainTitle.style.opacity = '0';
        
        setTimeout(() => {
            mainTitle.textContent = titles[currentIndex];
            mainTitle.style.opacity = '1';
        }, 300);
    }, 5000);
    
    mainTitle.style.transition = 'opacity 0.3s ease';
}

// === COUNTER ANIMATIONS ===
function initializeCounters() {
    const counters = document.querySelectorAll('.value-number[data-target]');
    
    counters.forEach(counter => {
        const target = parseFloat(counter.getAttribute('data-target'));
        const duration = 2000;
        const start = performance.now();
        
        function updateCounter(currentTime) {
            const elapsed = currentTime - start;
            const progress = Math.min(elapsed / duration, 1);
            
            // Easing function
            const easeOut = 1 - Math.pow(1 - progress, 3);
            const current = easeOut * target;
            
            counter.textContent = current.toFixed(target % 1 === 0 ? 0 : 1);
            
            if (progress < 1) {
                requestAnimationFrame(updateCounter);
            }
        }
        
        requestAnimationFrame(updateCounter);
    });
}

// === CHART INITIALIZATION ===
function initializeCharts() {
    initializePerformanceChart();
    initializeDriftChart();
    initializeCostChart();
    initializeMiniCharts();
    initialize3DTopology();
}

function initializeChartsForTab(tabName) {
    if (tabName === 'overview') {
        initializePerformanceChart();
    } else if (tabName === 'drift') {
        initializeDriftChart();
    } else if (tabName === 'resources') {
        initializeCostChart();
        initializeMiniCharts();
    }
}

function initializePerformanceChart() {
    const canvas = document.getElementById('performanceChart');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    const width = canvas.width = canvas.offsetWidth;
    const height = canvas.height = canvas.offsetHeight;
    
    // Generate sample data
    const dataPoints = 30;
    const data = Array.from({ length: dataPoints }, (_, i) => ({
        x: i,
        y: 70 + Math.sin(i * 0.3) * 20 + Math.random() * 10
    }));
    
    function draw() {
        ctx.clearRect(0, 0, width, height);
        
        // Draw grid
        ctx.strokeStyle = 'rgba(139, 92, 246, 0.1)';
        ctx.lineWidth = 1;
        for (let i = 0; i < 5; i++) {
            const y = (height / 4) * i;
            ctx.beginPath();
            ctx.moveTo(0, y);
            ctx.lineTo(width, y);
            ctx.stroke();
        }
        
        // Draw line
        const xScale = width / (dataPoints - 1);
        const yScale = height / 100;
        
        ctx.beginPath();
        ctx.strokeStyle = '#8B5CF6';
        ctx.lineWidth = 3;
        ctx.shadowBlur = 15;
        ctx.shadowColor = '#8B5CF6';
        
        data.forEach((point, i) => {
            const x = i * xScale;
            const y = height - (point.y * yScale);
            
            if (i === 0) {
                ctx.moveTo(x, y);
            } else {
                ctx.lineTo(x, y);
            }
        });
        ctx.stroke();
        
        // Draw gradient fill
        const gradient = ctx.createLinearGradient(0, 0, 0, height);
        gradient.addColorStop(0, 'rgba(139, 92, 246, 0.3)');
        gradient.addColorStop(1, 'rgba(139, 92, 246, 0)');
        
        ctx.fillStyle = gradient;
        ctx.lineTo(width, height);
        ctx.lineTo(0, height);
        ctx.closePath();
        ctx.fill();
        
        // Draw points
        data.forEach((point, i) => {
            const x = i * xScale;
            const y = height - (point.y * yScale);
            
            ctx.beginPath();
            ctx.arc(x, y, 4, 0, Math.PI * 2);
            ctx.fillStyle = '#00F0FF';
            ctx.shadowBlur = 10;
            ctx.shadowColor = '#00F0FF';
            ctx.fill();
        });
    }
    
    draw();
    state.charts.performance = { canvas, ctx, data, draw };
    
    // Animate
    setInterval(() => {
        data.shift();
        data.push({
            x: dataPoints - 1,
            y: 70 + Math.sin(Date.now() * 0.001) * 20 + Math.random() * 10
        });
        draw();
    }, 2000);
}

function initializeDriftChart() {
    const canvas = document.getElementById('driftChart');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    const width = canvas.width = canvas.offsetWidth;
    const height = canvas.height = canvas.offsetHeight;
    
    // Generate distribution data
    const bins = 50;
    const baseline = Array.from({ length: bins }, (_, i) => {
        const x = (i / bins) * 10 - 5;
        return Math.exp(-0.5 * x * x) * 100;
    });
    
    const current = Array.from({ length: bins }, (_, i) => {
        const x = (i / bins) * 10 - 5.5; // Slight shift
        return Math.exp(-0.5 * x * x) * 90 + Math.random() * 10;
    });
    
    function draw() {
        ctx.clearRect(0, 0, width, height);
        
        const barWidth = width / bins;
        
        // Draw baseline
        ctx.fillStyle = 'rgba(139, 92, 246, 0.3)';
        baseline.forEach((value, i) => {
            const barHeight = (value / 100) * height * 0.8;
            ctx.fillRect(i * barWidth, height - barHeight, barWidth - 1, barHeight);
        });
        
        // Draw current
        ctx.fillStyle = 'rgba(0, 240, 255, 0.5)';
        current.forEach((value, i) => {
            const barHeight = (value / 100) * height * 0.8;
            ctx.fillRect(i * barWidth, height - barHeight, barWidth - 1, barHeight);
        });
        
        // Legend
        ctx.font = '12px Inter';
        ctx.fillStyle = '#8B5CF6';
        ctx.fillText('Baseline', 20, 30);
        ctx.fillStyle = '#00F0FF';
        ctx.fillText('Current', 20, 50);
    }
    
    draw();
}

function initializeCostChart() {
    const canvas = document.getElementById('costChart');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    const width = canvas.width = canvas.offsetWidth;
    const height = canvas.height = canvas.offsetHeight;
    
    const data = [
        { label: 'Compute', value: 45, color: '#8B5CF6' },
        { label: 'Storage', value: 25, color: '#00F0FF' },
        { label: 'Network', value: 15, color: '#A855F7' },
        { label: 'Other', value: 15, color: '#6366F1' }
    ];
    
    function draw() {
        ctx.clearRect(0, 0, width, height);
        
        const centerX = width / 2;
        const centerY = height / 2;
        const radius = Math.min(width, height) / 2 - 40;
        
        let startAngle = -Math.PI / 2;
        const total = data.reduce((sum, item) => sum + item.value, 0);
        
        data.forEach((item, index) => {
            const sliceAngle = (item.value / total) * 2 * Math.PI;
            const endAngle = startAngle + sliceAngle;
            
            // Draw slice
            ctx.beginPath();
            ctx.moveTo(centerX, centerY);
            ctx.arc(centerX, centerY, radius, startAngle, endAngle);
            ctx.closePath();
            ctx.fillStyle = item.color;
            ctx.fill();
            
            // Draw glow
            ctx.shadowBlur = 15;
            ctx.shadowColor = item.color;
            ctx.fill();
            ctx.shadowBlur = 0;
            
            // Draw label
            const labelAngle = startAngle + sliceAngle / 2;
            const labelX = centerX + Math.cos(labelAngle) * (radius + 30);
            const labelY = centerY + Math.sin(labelAngle) * (radius + 30);
            
            ctx.fillStyle = '#e0e0e0';
            ctx.font = '12px Inter';
            ctx.textAlign = 'center';
            ctx.fillText(`${item.label} ${item.value}%`, labelX, labelY);
            
            startAngle = endAngle;
        });
    }
    
    draw();
}

function initializeMiniCharts() {
    const miniChartIds = ['cpuMiniChart', 'memMiniChart', 'gpuMiniChart', 'netMiniChart'];
    
    miniChartIds.forEach((id, index) => {
        const canvas = document.getElementById(id);
        if (!canvas) return;
        
        const ctx = canvas.getContext('2d');
        const width = canvas.width = canvas.offsetWidth;
        const height = canvas.height = canvas.offsetHeight;
        
        const points = 20;
        const data = Array.from({ length: points }, () => Math.random() * 100);
        
        function draw() {
            ctx.clearRect(0, 0, width, height);
            
            const xScale = width / (points - 1);
            const yScale = height / 100;
            
            // Area gradient
            const gradient = ctx.createLinearGradient(0, 0, 0, height);
            gradient.addColorStop(0, 'rgba(0, 240, 255, 0.3)');
            gradient.addColorStop(1, 'rgba(0, 240, 255, 0)');
            
            ctx.beginPath();
            data.forEach((value, i) => {
                const x = i * xScale;
                const y = height - (value * yScale);
                
                if (i === 0) {
                    ctx.moveTo(x, y);
                } else {
                    ctx.lineTo(x, y);
                }
            });
            ctx.lineTo(width, height);
            ctx.lineTo(0, height);
            ctx.closePath();
            ctx.fillStyle = gradient;
            ctx.fill();
            
            // Line
            ctx.beginPath();
            data.forEach((value, i) => {
                const x = i * xScale;
                const y = height - (value * yScale);
                
                if (i === 0) {
                    ctx.moveTo(x, y);
                } else {
                    ctx.lineTo(x, y);
                }
            });
            ctx.strokeStyle = '#00F0FF';
            ctx.lineWidth = 2;
            ctx.stroke();
        }
        
        draw();
        
        // Animate
        setInterval(() => {
            data.shift();
            data.push(Math.random() * 100);
            draw();
        }, 1000 + index * 200);
    });
}

function initialize3DTopology() {
    const canvas = document.getElementById('topologyCanvas');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
    
    // Simple 3D node visualization
    const nodes = [];
    for (let i = 0; i < 20; i++) {
        nodes.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            z: Math.random() * 100,
            vx: (Math.random() - 0.5) * 2,
            vy: (Math.random() - 0.5) * 2,
            vz: (Math.random() - 0.5) * 2,
            radius: 5 + Math.random() * 5
        });
    }
    
    function draw3D() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Update and draw nodes
        nodes.forEach(node => {
            node.x += node.vx;
            node.y += node.vy;
            node.z += node.vz;
            
            if (node.x < 0 || node.x > canvas.width) node.vx *= -1;
            if (node.y < 0 || node.y > canvas.height) node.vy *= -1;
            if (node.z < 0 || node.z > 100) node.vz *= -1;
            
            const scale = 1 + node.z / 100;
            const size = node.radius * scale;
            const opacity = 0.3 + (node.z / 100) * 0.7;
            
            ctx.beginPath();
            ctx.arc(node.x, node.y, size, 0, Math.PI * 2);
            ctx.fillStyle = `rgba(139, 92, 246, ${opacity})`;
            ctx.shadowBlur = 20;
            ctx.shadowColor = '#8B5CF6';
            ctx.fill();
        });
        
        // Draw connections
        nodes.forEach((node1, i) => {
            nodes.forEach((node2, j) => {
                if (i < j) {
                    const dx = node1.x - node2.x;
                    const dy = node1.y - node2.y;
                    const distance = Math.sqrt(dx * dx + dy * dy);
                    
                    if (distance < 150) {
                        ctx.beginPath();
                        ctx.moveTo(node1.x, node1.y);
                        ctx.lineTo(node2.x, node2.y);
                        ctx.strokeStyle = `rgba(0, 240, 255, ${0.2 * (1 - distance / 150)})`;
                        ctx.lineWidth = 1;
                        ctx.stroke();
                    }
                }
            });
        });
        
        requestAnimationFrame(draw3D);
    }
    
    draw3D();
    
    // Rotate button
    const rotateBtn = document.getElementById('rotate3D');
    if (rotateBtn) {
        rotateBtn.addEventListener('click', () => {
            nodes.forEach(node => {
                node.vx = (Math.random() - 0.5) * 4;
                node.vy = (Math.random() - 0.5) * 4;
                node.vz = (Math.random() - 0.5) * 4;
            });
        });
    }
}

// === COLOR PICKER ===
function initializeColorPickers() {
    const colorPickerBtns = document.querySelectorAll('.color-picker-btn');
    const modal = document.getElementById('colorPickerModal');
    const closeBtn = document.getElementById('closeColorPicker');
    
    colorPickerBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            state.currentChart = btn.getAttribute('data-chart');
            modal.classList.add('active');
        });
    });
    
    if (closeBtn) {
        closeBtn.addEventListener('click', () => {
            modal.classList.remove('active');
        });
    }
    
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.classList.remove('active');
        }
    });
    
    const colorOptions = document.querySelectorAll('.color-option');
    colorOptions.forEach(option => {
        option.addEventListener('click', () => {
            const scheme = option.getAttribute('data-scheme');
            applyColorScheme(scheme);
            modal.classList.remove('active');
        });
    });
}

function applyColorScheme(scheme) {
    const colors = state.colorSchemes[scheme];
    if (!colors) return;
    
    // Update chart colors
    document.documentElement.style.setProperty('--electric-violet', colors[0]);
    document.documentElement.style.setProperty('--cosmic-blue', colors[1]);
    document.documentElement.style.setProperty('--zen-purple', colors[2]);
    
    // Redraw charts
    Object.values(state.charts).forEach(chart => {
        if (chart.draw) chart.draw();
    });
    
    console.log(`Applied ${scheme} color scheme`);
}

// === INTERACTIONS ===
function initializeInteractions() {
    // File tree expansion
    const nodeHeaders = document.querySelectorAll('.node-header[data-expanded]');
    nodeHeaders.forEach(header => {
        header.addEventListener('click', () => {
            const expanded = header.getAttribute('data-expanded') === 'true';
            header.setAttribute('data-expanded', !expanded);
            
            const children = header.nextElementSibling;
            if (children && children.classList.contains('node-children')) {
                children.style.display = expanded ? 'none' : 'block';
            }
        });
    });
    
    // Scan project button
    const scanBtn = document.getElementById('scanProjectBtn');
    if (scanBtn) {
        scanBtn.addEventListener('click', () => {
            scanBtn.innerHTML = '<span>⏳</span> Scanning...';
            scanBtn.disabled = true;
            
            setTimeout(() => {
                scanBtn.innerHTML = '<span>✓</span> Scan Complete';
                setTimeout(() => {
                    scanBtn.innerHTML = '<span>🔍</span> Deep Scan';
                    scanBtn.disabled = false;
                }, 2000);
            }, 3000);
        });
    }
    
    // Mini chart animations
    const miniCharts = document.querySelectorAll('.mini-chart');
    miniCharts.forEach(chart => {
        chart.addEventListener('mouseenter', () => {
            chart.style.transform = 'scale(1.05)';
            chart.style.transition = 'transform 0.3s ease';
        });
        
        chart.addEventListener('mouseleave', () => {
            chart.style.transform = 'scale(1)';
        });
    });
}

// === REAL-TIME UPDATES ===
function startRealTimeUpdates() {
    setInterval(() => {
        updateSystemMetrics();
    }, 5000);
}

function updateSystemMetrics() {
    // Simulate real-time metric updates
    const metrics = [
        { selector: '.health-fill[data-status="excellent"]', min: 90, max: 100 },
        { selector: '.health-fill[data-status="good"]', min: 80, max: 95 }
    ];
    
    metrics.forEach(metric => {
        const elements = document.querySelectorAll(metric.selector);
        elements.forEach(el => {
            const newValue = Math.floor(Math.random() * (metric.max - metric.min) + metric.min);
            el.style.width = `${newValue}%`;
            el.parentElement.nextElementSibling.textContent = `${newValue}%`;
        });
    });
}

// === UTILITY FUNCTIONS ===
function formatNumber(num) {
    if (num >= 1000000) {
        return (num / 1000000).toFixed(1) + 'M';
    } else if (num >= 1000) {
        return (num / 1000).toFixed(1) + 'K';
    }
    return num.toString();
}

function getRandomColor() {
    const colors = ['#8B5CF6', '#00F0FF', '#A855F7', '#6366F1', '#10B981'];
    return colors[Math.floor(Math.random() * colors.length)];
}

// === KEYBOARD SHORTCUTS ===
document.addEventListener('keydown', (e) => {
    // Tab navigation with numbers 1-5
    if (e.key >= '1' && e.key <= '5') {
        const tabs = ['overview', 'lineage', 'drift', 'pipeline', 'resources'];
        switchTab(tabs[parseInt(e.key) - 1]);
    }
    
    // ESC to close modal
    if (e.key === 'Escape') {
        const modal = document.getElementById('colorPickerModal');
        if (modal) modal.classList.remove('active');
    }
});

// === CONSOLE GREETING ===
console.log('%c 🚀 DEEP SPACE FUSION MLOps Dashboard ', 
    'background: linear-gradient(135deg, #8B5CF6, #00F0FF); color: white; padding: 10px 20px; font-size: 16px; font-weight: bold;');
console.log('%c Advanced AI Operations Control Center', 
    'color: #8B5CF6; font-size: 12px;');
console.log('%c Keyboard Shortcuts: 1-5 (Switch Tabs) | ESC (Close Modal)', 
    'color: #00F0FF; font-size: 10px;');

// === EXPORT ===
window.MLOpsDashboard = {
    state,
    switchTab,
    applyColorScheme,
    updateSystemMetrics
};
